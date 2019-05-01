#
# PySNMP MIB module A100-R1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A100-R1-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:03:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, IpAddress, NotificationType, MibIdentifier, Bits, Gauge32, enterprises, Integer32, ModuleIdentity, TimeTicks, Unsigned32, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "IpAddress", "NotificationType", "MibIdentifier", "Bits", "Gauge32", "enterprises", "Integer32", "ModuleIdentity", "TimeTicks", "Unsigned32", "ObjectIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nec = MibIdentifier((1, 3, 6, 1, 4, 1, 119))
nec_mib = MibIdentifier((1, 3, 6, 1, 4, 1, 119, 2)).setLabel("nec-mib")
necProductDepend = MibIdentifier((1, 3, 6, 1, 4, 1, 119, 2, 3))
atomis_mib = MibIdentifier((1, 3, 6, 1, 4, 1, 119, 2, 3, 14)).setLabel("atomis-mib")
m5core_mib = MibIdentifier((1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3)).setLabel("m5core-mib")
node = MibIdentifier((1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 1))
linf = MibIdentifier((1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 2))
conn = MibIdentifier((1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 3))
perf = MibIdentifier((1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 4))
nodeOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("down", 1), ("active", 2), ("off-line", 3), ("testing", 4), ("initializing", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: nodeOperStatus.setDescription('Operational status of the Model 5.')
nodeIfConfTable = MibTable((1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 1, 2), )
if mibBuilder.loadTexts: nodeIfConfTable.setStatus('mandatory')
if mibBuilder.loadTexts: nodeIfConfTable.setDescription('Configuration of the line cards.')
nodeIfConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 1, 2, 1), ).setIndexNames((0, "A100-R1-MIB", "nodeIfConfIndex"))
if mibBuilder.loadTexts: nodeIfConfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: nodeIfConfEntry.setDescription('-')
nodeIfConfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeIfConfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: nodeIfConfIndex.setDescription('The index of the table.')
nodeIfConfPhysType = MibTableColumn((1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 99))).clone(namedValues=NamedValues(("other", 1), ("sar", 2), ("taxi100M", 3), ("oc3cSMF", 4), ("oc-3cMMF", 5), ("ds3-PLCP-SCRAMBLE", 6), ("ds3-PLCP-noScramble", 7), ("relay-6Mcel", 8), ("notInstalled", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeIfConfPhysType.setStatus('mandatory')
if mibBuilder.loadTexts: nodeIfConfPhysType.setDescription('The PMD/physical layer format of the line cards.')
nodeIfConfRev = MibTableColumn((1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeIfConfRev.setStatus('mandatory')
if mibBuilder.loadTexts: nodeIfConfRev.setDescription('The revision of the line cards. Implemented by JUL/1994.')
nodeIfConfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 99))).clone(namedValues=NamedValues(("other", 1), ("inService", 2), ("outOfService", 3), ("testing", 4), ("localLoopBack", 5), ("remoteLoopBack", 6), ("notInstalled", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeIfConfStatus.setStatus('mandatory')
if mibBuilder.loadTexts: nodeIfConfStatus.setDescription('Operational status of the line cards.')
nodeFanStatus = MibScalar((1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeFanStatus.setStatus('mandatory')
if mibBuilder.loadTexts: nodeFanStatus.setDescription('Operational status of the FAN.')
nodeUpcWindowSize = MibScalar((1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 120))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nodeUpcWindowSize.setStatus('mandatory')
if mibBuilder.loadTexts: nodeUpcWindowSize.setDescription('UPC window size. Integer Wi represents Wi X 512 cell time. Wi=1 correspond to 1.4msec. Wi=120 correspond to 168msec. It is not allowed to change window size when the PVC is exsisting.')
nodeBestEffortBufferSize = MibScalar((1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nodeBestEffortBufferSize.setStatus('mandatory')
if mibBuilder.loadTexts: nodeBestEffortBufferSize.setDescription('Input buffer capacity for Best Effort traffic(Bb). The number of cells stored in the buffer is Bb X 128. The default value is 0. The sum of the buffer capacity is 2047 cells.')
nodeGuaranteedBufferSize = MibScalar((1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nodeGuaranteedBufferSize.setStatus('mandatory')
if mibBuilder.loadTexts: nodeGuaranteedBufferSize.setDescription('Input buffer capacity for Guaranteed traffic(Bg). The number of cells stored in the buffer is Bg X 128. The default value is 0. The sum of the buffer capacity is 2047 cells.')
nodeBestEffortBufferThreshold = MibScalar((1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nodeBestEffortBufferThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: nodeBestEffortBufferThreshold.setDescription('Threshold buffer capacity for Best Effort traffic. If the number of cells stored in the buffer exceeds this threshold, cells with CLP=1 and traffic defined as UBR will be discarded.')
nodeGuaranteedBufferThreshold = MibScalar((1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nodeGuaranteedBufferThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: nodeGuaranteedBufferThreshold.setDescription('Threshold buffer capacity for Guaranteed traffic. If the number of cells stored in the buffer exceeds this threshold, cells with CLP=1 and traffic defined as VBR will be discarded.')
nodeSaveConf = MibScalar((1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("save", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: nodeSaveConf.setStatus('mandatory')
if mibBuilder.loadTexts: nodeSaveConf.setDescription('Save system configuration information including PVC/SVC table to the non-volatile memory. save(1) shall be written in case of saving the configiration data.')
nodeSaveResult = MibScalar((1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("temporaryFailure", 1), ("notReady", 2), ("ready", 3), ("succeed", 4), ("nearend", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeSaveResult.setStatus('mandatory')
if mibBuilder.loadTexts: nodeSaveResult.setDescription('Show the result of the save command issued from NMS. The result is either Succeed/temporary failure/notReady. nearend will be returned if the number of access times has exceeded the limit.')
linfStatusTable = MibTable((1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 2, 1), )
if mibBuilder.loadTexts: linfStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: linfStatusTable.setDescription('Status of the line card including ATM specific information.')
linfStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 2, 1, 1), ).setIndexNames((0, "A100-R1-MIB", "linfIndex"))
if mibBuilder.loadTexts: linfStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: linfStatusEntry.setDescription(' - ')
linfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: linfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: linfIndex.setDescription(' - ')
linfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 99))).clone(namedValues=NamedValues(("normal", 1), ("los", 2), ("lof", 3), ("loc", 4), ("ais", 5), ("yellow-line", 6), ("yellow-path", 7), ("lop", 8), ("notInstalled", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: linfStatus.setStatus('mandatory')
if mibBuilder.loadTexts: linfStatus.setDescription('Status of the line cards')
linfConf = MibTableColumn((1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 99))).clone(namedValues=NamedValues(("public-UNI", 1), ("private-UNI", 2), ("private-NNI", 3), ("others", 99)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: linfConf.setStatus('mandatory')
if mibBuilder.loadTexts: linfConf.setDescription('Line card type.')
mibBuilder.exportSymbols("A100-R1-MIB", nodeIfConfTable=nodeIfConfTable, linfStatusEntry=linfStatusEntry, nodeGuaranteedBufferThreshold=nodeGuaranteedBufferThreshold, nodeIfConfStatus=nodeIfConfStatus, nodeOperStatus=nodeOperStatus, nodeFanStatus=nodeFanStatus, nec_mib=nec_mib, perf=perf, nodeIfConfPhysType=nodeIfConfPhysType, linfStatus=linfStatus, nodeBestEffortBufferSize=nodeBestEffortBufferSize, linfStatusTable=linfStatusTable, nodeIfConfEntry=nodeIfConfEntry, m5core_mib=m5core_mib, linfIndex=linfIndex, nodeGuaranteedBufferSize=nodeGuaranteedBufferSize, nodeIfConfRev=nodeIfConfRev, nec=nec, linf=linf, nodeUpcWindowSize=nodeUpcWindowSize, node=node, conn=conn, necProductDepend=necProductDepend, linfConf=linfConf, nodeIfConfIndex=nodeIfConfIndex, nodeSaveResult=nodeSaveResult, nodeBestEffortBufferThreshold=nodeBestEffortBufferThreshold, nodeSaveConf=nodeSaveConf, atomis_mib=atomis_mib)