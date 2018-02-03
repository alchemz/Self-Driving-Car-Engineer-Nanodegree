#batches
import math
def batches(batch_size, feature, labels):
	asset len(features)== len(labels)
	output_batches = []

	sample_size = len(features)
	for start_i in range(0, sample_size, batch_szie):
		end_i = start_i + batch_size
		batch = [features[start_i:end_i], labels[start_i:end_i]]
		output_batches.append(batch)
	return output_batches