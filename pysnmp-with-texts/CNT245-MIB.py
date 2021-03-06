#
# PySNMP MIB module CNT245-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CNT245-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:25:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Bits, enterprises, iso, Unsigned32, MibIdentifier, ObjectIdentity, Counter32, IpAddress, Counter64, NotificationType, Integer32, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Bits", "enterprises", "iso", "Unsigned32", "MibIdentifier", "ObjectIdentity", "Counter32", "IpAddress", "Counter64", "NotificationType", "Integer32", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cnt2Compression = ModuleIdentity((1, 3, 6, 1, 4, 1, 333, 2, 4, 5))
if mibBuilder.loadTexts: cnt2Compression.setLastUpdated('0110011200Z')
if mibBuilder.loadTexts: cnt2Compression.setOrganization('Computer Network Technology Corporation')
if mibBuilder.loadTexts: cnt2Compression.setContactInfo('<intentionaly left out>')
if mibBuilder.loadTexts: cnt2Compression.setDescription('This defines the CNT Compression Engine MIB')
cnt2CompressionTable = MibTable((1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 1), )
if mibBuilder.loadTexts: cnt2CompressionTable.setStatus('current')
if mibBuilder.loadTexts: cnt2CompressionTable.setDescription('A list of compression/decompression engines on this system.')
cnt2CompressionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 1, 1), ).setIndexNames((0, "CNT245-MIB", "cnt2CompressionSlotIndex"), (0, "CNT245-MIB", "cnt2CompressionIndex"))
if mibBuilder.loadTexts: cnt2CompressionEntry.setStatus('current')
if mibBuilder.loadTexts: cnt2CompressionEntry.setDescription('An instance of a compression/decompression.')
cnt2CompressionSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2CompressionSlotIndex.setStatus('current')
if mibBuilder.loadTexts: cnt2CompressionSlotIndex.setDescription('The slot number where this compression/ decompression was done. This index matches cnt2SlotIndex.')
cnt2CompressionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2CompressionIndex.setStatus('current')
if mibBuilder.loadTexts: cnt2CompressionIndex.setDescription('The relative instance of the compression/decompression engine for this slot. This index is always 1.')
cnt2BytesToCompress = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2BytesToCompress.setStatus('current')
if mibBuilder.loadTexts: cnt2BytesToCompress.setDescription('The number of bytes submitted to the engine for compression. This value will include all bytes submitted whether or not compression was successful. This value will always be equal or larger than cnt2CompressedBytes.')
cnt2CompressedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2CompressedBytes.setStatus('current')
if mibBuilder.loadTexts: cnt2CompressedBytes.setDescription('The number of bytes received from the engine after compression. This value will include all of the bytes received from the engine whether or not compres- sion was successful, since the engine returns the initial size in any unsucces- sful attempt at compression. This value will be equal or smaller than cnt2BytesToCompress.')
cnt2BytesToDecompress = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2BytesToDecompress.setStatus('current')
if mibBuilder.loadTexts: cnt2BytesToDecompress.setDescription('The number of bytes submitted to the engine for decompression. This value will include all bytes submitted whether or not decompression was successful. This value will always be equal or smaller than cnt2DecompressedBytes.')
cnt2DecompressedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2DecompressedBytes.setStatus('current')
if mibBuilder.loadTexts: cnt2DecompressedBytes.setDescription('The number of bytes received from the engine after decompression. This value will include all of the bytes received from the engine whether or not decompres- sion was successful, since the engine returns the initial size in any unsucces- sful attempt at decompression. This value will be equal or larger than cnt2BytesToDecompress.')
cnt2ifCompressionNumber = MibScalar((1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2ifCompressionNumber.setStatus('current')
if mibBuilder.loadTexts: cnt2ifCompressionNumber.setDescription('The number of interfaces using compression/ decompression in this system.')
cnt2ifCompressionTable = MibTable((1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 3), )
if mibBuilder.loadTexts: cnt2ifCompressionTable.setStatus('current')
if mibBuilder.loadTexts: cnt2ifCompressionTable.setDescription('A list of interface entries using compression/ decompression in this system. The number of entries is given by cnt2ifCompressionNumber.')
cnt2ifCompressionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 3, 1), ).setIndexNames((0, "CNT245-MIB", "cnt2ifCompressionSlotIndex"), (0, "CNT245-MIB", "cnt2ifCompressionIndex"))
if mibBuilder.loadTexts: cnt2ifCompressionEntry.setStatus('current')
if mibBuilder.loadTexts: cnt2ifCompressionEntry.setDescription('An interface entry using compression/ decompression.')
cnt2ifCompressionSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2ifCompressionSlotIndex.setStatus('current')
if mibBuilder.loadTexts: cnt2ifCompressionSlotIndex.setDescription('The slot number where this compression was done. This index matches cnt2IfSlotIndex.')
cnt2ifCompressionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2ifCompressionIndex.setStatus('current')
if mibBuilder.loadTexts: cnt2ifCompressionIndex.setDescription('The local interface index on which this compression was done. This index matches cnt2IfIndex.')
cnt2ifCompressedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 3, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2ifCompressedOctets.setStatus('current')
if mibBuilder.loadTexts: cnt2ifCompressedOctets.setDescription('The number of bytes that were compressed out of the transmitted data stream. To calculate the compression ratio for trans- mitted data, the following calculation would be used: ifOutOctets + cnt2ifCompressedOctets ------------------------------------ ifOutOctets. to calculate the overall compression for this interface, the following calculation would be used: ifOutOctets + cnt2ifCompressedOctets + cnt2ifDecompressedOctets + ifInOctets -------------------------------------- ifOutOctets + ifInOctets.')
cnt2ifCompressionRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2ifCompressionRatio.setStatus('current')
if mibBuilder.loadTexts: cnt2ifCompressionRatio.setDescription('The Compression ratio for this index. The value is represent of 1 to xx.xx Compression Ratio. Example: Ratio of 1:15.82 would have this set to a value of 1582. The internal Calculation is done as: 100 * (ifOutOctets + cnt2ifCompressedOctets) --------------------------------------------- ifOutOctets Then the result is mod by 100 for floating point. This OID gets created dynamically when there is a compression circuit active.')
cnt2ifDecompressionTable = MibTable((1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 4), )
if mibBuilder.loadTexts: cnt2ifDecompressionTable.setStatus('current')
if mibBuilder.loadTexts: cnt2ifDecompressionTable.setDescription('A list of interface entries using decompression in this system. The number of entries is given by cnt2ifCompressionNumber.')
cnt2ifDecompressionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 4, 1), ).setIndexNames((0, "CNT245-MIB", "cnt2ifDecompressionSlotIndex"), (0, "CNT245-MIB", "cnt2ifDecompressionIndex"))
if mibBuilder.loadTexts: cnt2ifDecompressionEntry.setStatus('current')
if mibBuilder.loadTexts: cnt2ifDecompressionEntry.setDescription('An interface entry using decompression.')
cnt2ifDecompressionSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2ifDecompressionSlotIndex.setStatus('current')
if mibBuilder.loadTexts: cnt2ifDecompressionSlotIndex.setDescription('The slot number where this decompression was done. This index matches cnt2IfSlotIndex.')
cnt2ifDecompressionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2ifDecompressionIndex.setStatus('current')
if mibBuilder.loadTexts: cnt2ifDecompressionIndex.setDescription('The local interface index on which this decompression was done. This index matches cnt2IfIndex.')
cnt2ifDecompressedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 4, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2ifDecompressedOctets.setStatus('current')
if mibBuilder.loadTexts: cnt2ifDecompressedOctets.setDescription('The number of bytes that were compressed out of the received data stream. To calculate the compression ratio for received data, the following calculation would be used: ifInOctets + cnt2ifDeCompressedOctets ------------------------------------- ifInOctets to calculate the overall compression for this interface, the following calculation would be used: ifOutOctets + cnt2ifCompressedOctets + cnt2ifDecompressedOctets + ifInOctets -------------------------------------- ifOutOctets + ifInOctets.')
cnt2ifDecompressionRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 5, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2ifDecompressionRatio.setStatus('current')
if mibBuilder.loadTexts: cnt2ifDecompressionRatio.setDescription('The Decompression ratio for this index. The value is represent 1 to xx.xx decompression Ratio. Example: Ratio of 13.82 :1 would have this set to a value of 1382. The internal Calculation is done as: 100 * (ifInOctets + cnt2ifDeCompressedOctets) --------------------------------------------- ifInOctets Then the result is mod by 100 for floating point. This OID gets created dynamically when there is a decompression circuit active.')
mibBuilder.exportSymbols("CNT245-MIB", cnt2CompressionSlotIndex=cnt2CompressionSlotIndex, cnt2ifCompressedOctets=cnt2ifCompressedOctets, cnt2DecompressedBytes=cnt2DecompressedBytes, cnt2ifCompressionIndex=cnt2ifCompressionIndex, cnt2ifCompressionTable=cnt2ifCompressionTable, cnt2BytesToDecompress=cnt2BytesToDecompress, cnt2ifDecompressionRatio=cnt2ifDecompressionRatio, cnt2CompressionTable=cnt2CompressionTable, cnt2CompressionEntry=cnt2CompressionEntry, cnt2ifDecompressionTable=cnt2ifDecompressionTable, cnt2ifDecompressedOctets=cnt2ifDecompressedOctets, cnt2ifDecompressionSlotIndex=cnt2ifDecompressionSlotIndex, cnt2ifCompressionSlotIndex=cnt2ifCompressionSlotIndex, cnt2CompressedBytes=cnt2CompressedBytes, cnt2CompressionIndex=cnt2CompressionIndex, cnt2ifCompressionEntry=cnt2ifCompressionEntry, cnt2ifDecompressionEntry=cnt2ifDecompressionEntry, cnt2ifCompressionNumber=cnt2ifCompressionNumber, cnt2Compression=cnt2Compression, cnt2BytesToCompress=cnt2BytesToCompress, cnt2ifDecompressionIndex=cnt2ifDecompressionIndex, cnt2ifCompressionRatio=cnt2ifCompressionRatio, PYSNMP_MODULE_ID=cnt2Compression)
