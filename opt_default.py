import tensorflow as tf

FLAGS = tf.compat.v1.flags.FLAGS


"----------------------------- Training options -----------------------------"
tf.compat.v1.flags.DEFINE_integer("batch", 8, "batch size")
tf.compat.v1.flags.DEFINE_integer("testbatch", 64, "test batch size")
tf.compat.v1.flags.DEFINE_integer("epoch", 30, "Current epoch")
tf.compat.v1.flags.DEFINE_integer("fromStep", 0, "Initial epoch")
tf.compat.v1.flags.DEFINE_integer("SAVE_EVERY", 1, "tensorboard save")
tf.compat.v1.flags.DEFINE_integer("TEST_EVERY", 1, "tensorboard test")
tf.compat.v1.flags.DEFINE_float("eval_thresh", 0.5, "eval_thresh test")
tf.compat.v1.flags.DEFINE_integer("VIZ_EVERY", 100, "tensorboard viz")
tf.compat.v1.flags.DEFINE_integer("total_traindata", 24980, "total_traindata")#mpii:24984

tf.compat.v1.flags.DEFINE_string("Model_folder_name", 'resnet18', "Model_folder_name")

tf.compat.v1.flags.DEFINE_boolean("Early_stopping",False,"early stop or not")
tf.compat.v1.flags.DEFINE_boolean('isTrain', True, 'trainable or not')
tf.compat.v1.flags.DEFINE_boolean('isTrainpre',True,'if pre train,set false')
tf.compat.v1.flags.DEFINE_boolean('offset', True, 'offset')
tf.compat.v1.flags.DEFINE_boolean('DUC', True, 'duc')
tf.compat.v1.flags.DEFINE_integer('Shuffle', 4, 'depth_to_space:2/4')


tf.compat.v1.flags.DEFINE_string("backbone", 'resnet18', "backbone:mobilenetv1/mobilenetv2"
                                                      "/mobilenetXT/mobilenetv3/hourglass/efficientnet/resnet18")
tf.compat.v1.flags.DEFINE_string("modeloutputFile", 'MPII', "model output dir")
tf.compat.v1.flags.DEFINE_string("checkpoints_file", None, " checkpoints file")
tf.compat.v1.flags.DEFINE_string("checkpoinsaveDir", 'MPII', " checkpoints save dir")
tf.compat.v1.flags.DEFINE_string("train_all_result", 'Result/MPII', "model name")



"----------------------------- Data options -----------------------------"
tf.compat.v1.flags.DEFINE_boolean("checkanno", False,"check annotation")

tf.compat.v1.flags.DEFINE_string("dataset",'MPII_13',"choose data format:MPII_13/MPII/COCO/YOGA")
tf.compat.v1.flags.DEFINE_integer("totaljoints", 13, "MPII16/MPII_13/COCO13/YOGA13")

tf.compat.v1.flags.DEFINE_integer("inputResH", 224, "Input image height")
tf.compat.v1.flags.DEFINE_integer("inputResW", 224, "Input image width")
tf.compat.v1.flags.DEFINE_integer("outputResH", 56, "Output image height")
tf.compat.v1.flags.DEFINE_integer("outputResW", 56, "Output image width")

tf.compat.v1.flags.DEFINE_boolean('grayimage', False, 'image type')


"----------------------------- Hyperparameter options -----------------------------"
#lr
tf.compat.v1.flags.DEFINE_string("lr_type", "exponential_decay","exponential_decay|polynomial_decay|inverse_time_decay|cosine_decay")
tf.compat.v1.flags.DEFINE_float("lr", 0.001, "learning rate")
tf.compat.v1.flags.DEFINE_float("decay_rate", 0.98, "learning rate decay rate")
tf.compat.v1.flags.DEFINE_integer("decay_steps", 5000, "learning rate decay steps")

#optimizer
tf.compat.v1.flags.DEFINE_float("epsilon", 1e-8, "epsilon")
tf.compat.v1.flags.DEFINE_string("optimizer", 'Gradient', "Adam/Momentum/Gradient")
tf.compat.v1.flags.DEFINE_float("momentum", 0.9, "Momentum value")

tf.compat.v1.flags.DEFINE_integer("gaussian_thres", 12, "gaussian threshold")
tf.compat.v1.flags.DEFINE_integer("gaussian_sigma", 6, "gaussian sigma")
tf.compat.v1.flags.DEFINE_integer("v3_width_scale", 1, "for mobilenetv3:0.35,0.5,0.75,1,1.25")
tf.compat.v1.flags.DEFINE_string("v3_version", 'small', "for mobilenetv3:small/large")

#ACTIVATE
tf.compat.v1.flags.DEFINE_string("activate_function", 'relu', "swish/relu")

#loss
tf.compat.v1.flags.DEFINE_integer("epsilon_loss", 2, "wing_loss(2)/AdapWingLoss(1)")
tf.compat.v1.flags.DEFINE_integer("w", 2, "wing_loss(10)/AdapWingLoss(14)")
tf.compat.v1.flags.DEFINE_string("hm_lossselect", 'l2', "l2/wing/adaptivewing/smooth_l1")

#EARLY STOPPING
tf.compat.v1.flags.DEFINE_integer("j_min", 5, "if j_num>j_min,begin to decay lr")
tf.compat.v1.flags.DEFINE_integer("j_max", 10, "if j_num>j_max,stop training")
tf.compat.v1.flags.DEFINE_integer("test_epoch", 0, "每50轮迭代输出状态test")
tf.compat.v1.flags.DEFINE_integer("require_improvement",300, "如果在#轮内没有改进，停止迭代")

#model compression
tf.compat.v1.flags.DEFINE_integer("depth_multiplier", 1, "control the output channel")


"----------------------------- Eval options -----------------------------"
tf.compat.v1.flags.DEFINE_string("testdataset", "single_yoga2_test", "testdataset")
tf.compat.v1.flags.DEFINE_integer("inputsize", 224, "Input image")
tf.compat.v1.flags.DEFINE_string("Groundtru_annojson", 'poseval/data/gt/single_yoga2_test_gt.json', "Groundtru_annojson")
tf.compat.v1.flags.DEFINE_string("modelpath", './poseval/models/280/', "testing models path")
tf.compat.v1.flags.DEFINE_string("testing_path", 'poseval/img/single_yoga2_test', "testing dataset path")
tf.compat.v1.flags.DEFINE_string("resultpath", './poseval/results/', "result output path")



"----------------------------- Realtime testing options -----------------------------"
tf.compat.v1.flags.DEFINE_string("testmodel", "Result/MPII/resnet18/resnet18False2021-02-25-10-20-39.pb", "testmodel")
tf.compat.v1.flags.DEFINE_string("input_node_name", "Image:0", "input_node_name")
tf.compat.v1.flags.DEFINE_string("output_node_name", "network/Output:0", "output_node_name")
tf.compat.v1.flags.DEFINE_integer("modelinputsize", 224, "Input image")

opt = FLAGS


