#
# PySNMP MIB module HUAWEI-MIRROR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-MIRROR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:46:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
huaweiMgmt, = mibBuilder.importSymbols("HUAWEI-MIB", "huaweiMgmt")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Bits, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, ObjectIdentity, Unsigned32, MibIdentifier, ModuleIdentity, Integer32, Counter64, IpAddress, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "ObjectIdentity", "Unsigned32", "MibIdentifier", "ModuleIdentity", "Integer32", "Counter64", "IpAddress", "Gauge32")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
hwMirrorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 162))
if mibBuilder.loadTexts: hwMirrorMIB.setLastUpdated('200801012030Z')
if mibBuilder.loadTexts: hwMirrorMIB.setOrganization('Huawei Technologies co.,Ltd.')
if mibBuilder.loadTexts: hwMirrorMIB.setContactInfo('8090 Team Huawei Technologies co.,Ltd. Huawei Bld.,NO.3 Xinxi Rd., Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China http://www.huawei.com Zip:100085 ')
if mibBuilder.loadTexts: hwMirrorMIB.setDescription('MIB description of mirror.')
hwMirrorMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1))
hwLocalMirror = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1))
hwLocalObserveTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 1), )
if mibBuilder.loadTexts: hwLocalObserveTable.setStatus('current')
if mibBuilder.loadTexts: hwLocalObserveTable.setDescription(' The hwLocalObserveTable lists local mirror characters. ')
hwLocalObserveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 1, 1), ).setIndexNames((0, "HUAWEI-MIRROR-MIB", "hwLocalObservePort"))
if mibBuilder.loadTexts: hwLocalObserveEntry.setStatus('current')
if mibBuilder.loadTexts: hwLocalObserveEntry.setDescription(' The hwLocalObserveEntry lists local mirror characters. ')
hwLocalObservePort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hwLocalObservePort.setStatus('current')
if mibBuilder.loadTexts: hwLocalObservePort.setDescription('Ifindex is the index of the observing port and is used to search the name of an observing port.')
hwLocalObserveIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLocalObserveIndex.setStatus('current')
if mibBuilder.loadTexts: hwLocalObserveIndex.setDescription(' Index of an observing port that identifies the observing port. Single chassis: (The index of a physical port corresponds to the slot number of a board. The observe index ranges from 1 to 32.One board supports 32 logical observing ports.) Multi-chassis: Supports physical observing ports only. The observe index ranges from 1 to 128. ')
hwLocalObserveWithLinkLayerHeader = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLocalObserveWithLinkLayerHeader.setStatus('current')
if mibBuilder.loadTexts: hwLocalObserveWithLinkLayerHeader.setDescription(' Same interworking attribute. 1: different interworking, mirroring packets at and above the IP layer. 0: same interworking, mirroring packets at and above Layer 2. Default value: 1. ')
hwLocalObserveRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLocalObserveRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwLocalObserveRowStatus.setDescription(' Row status. The value ranges from 1 to 6 but usually 4 and 6 are used. createAndGo[4] - create a row. destroy[6] -delete a row. ')
hwLocalPortMirrorTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 2), )
if mibBuilder.loadTexts: hwLocalPortMirrorTable.setStatus('current')
if mibBuilder.loadTexts: hwLocalPortMirrorTable.setDescription(' The hwLocalPortMirrorTable lists local mirror characters. ')
hwLocalPortMirrorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 2, 1), ).setIndexNames((0, "HUAWEI-MIRROR-MIB", "hwLocalMirrorPort"))
if mibBuilder.loadTexts: hwLocalPortMirrorEntry.setStatus('current')
if mibBuilder.loadTexts: hwLocalPortMirrorEntry.setDescription(' The hwLocalPortMirrorEntry lists local mirror characters. ')
hwLocalMirrorPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hwLocalMirrorPort.setStatus('current')
if mibBuilder.loadTexts: hwLocalMirrorPort.setDescription('Ifindex of the mirroring port and is used to search the name of a mirroring port.')
hwLocalMirrorBearing = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inbound", 1), ("outbound", 2), ("inout", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLocalMirrorBearing.setStatus('current')
if mibBuilder.loadTexts: hwLocalMirrorBearing.setDescription('Mirroring direction: inbound, outbound, and in-out.1:inbound 2:outbound 3:in-out.')
hwLocalCpuPacketFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 2, 1, 3), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLocalCpuPacketFlag.setStatus('current')
if mibBuilder.loadTexts: hwLocalCpuPacketFlag.setDescription(' Indicates whether the packets sent to the CPU need to be mirrored. True: CPU packets are forwarded; False: CPU packets are not forwarded. You can configure this object only when the mirroring direction is 1 or 3. Default value: false. ')
hwLocalPortMirrorCar = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(100, 2500000), ))).setUnits('Kbps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLocalPortMirrorCar.setStatus('current')
if mibBuilder.loadTexts: hwLocalPortMirrorCar.setDescription(' CAR (CIR) of mirrored packets, expressed in thousand bits per second. The default value is 0, which indicates that CAR is not performed. ')
hwLocalPortMirrorRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLocalPortMirrorRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwLocalPortMirrorRowStatus.setDescription(' Row status. The value ranges from 1 to 6 but usually 4 and 6 are used. createAndGo[4] - create a row. destroy[6] -delete a row. ')
hwLocalFlowMirrorTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 3), )
if mibBuilder.loadTexts: hwLocalFlowMirrorTable.setStatus('current')
if mibBuilder.loadTexts: hwLocalFlowMirrorTable.setDescription(' The hwLocalFlowMirrorTable lists local mirror characters. ')
hwLocalFlowMirrorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 3, 1), ).setIndexNames((0, "HUAWEI-MIRROR-MIB", "hwLocalBehaviorName"))
if mibBuilder.loadTexts: hwLocalFlowMirrorEntry.setStatus('current')
if mibBuilder.loadTexts: hwLocalFlowMirrorEntry.setDescription(' The hwLocalFlowMirrorEntry lists local mirror characters. ')
hwLocalBehaviorName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 3, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31)))
if mibBuilder.loadTexts: hwLocalBehaviorName.setStatus('current')
if mibBuilder.loadTexts: hwLocalBehaviorName.setDescription('Traffic behavior view name.')
hwLocalFlowMirrorEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 3, 1, 2), EnabledStatus().clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLocalFlowMirrorEnable.setStatus('current')
if mibBuilder.loadTexts: hwLocalFlowMirrorEnable.setDescription(' Indicates whether the flow mirroring is enabled. Disable indicates that flow mirroring is disabled; Enable indicates that flow mirroring is enabled. Default value: disable. ')
hwLocalFlowMirrorCar = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(100, 2500000), ))).setUnits('Kbps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLocalFlowMirrorCar.setStatus('current')
if mibBuilder.loadTexts: hwLocalFlowMirrorCar.setDescription(' CAR (CIR) of mirrored packets, expressed in thousand bits per second. The default value is 0, which indicates that CAR is not performed. ')
hwLocalFlowMirrorRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLocalFlowMirrorRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwLocalFlowMirrorRowStatus.setDescription(' Row status. The value ranges from 1 to 6 but usually 4 and 6 are used. createAndGo[4] - create a row. destroy[6] -delete a row. ')
hwLocalSlotMirrorTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 4), )
if mibBuilder.loadTexts: hwLocalSlotMirrorTable.setStatus('current')
if mibBuilder.loadTexts: hwLocalSlotMirrorTable.setDescription(' The hwLocalSlotMirrorTable lists local mirror characters. ')
hwLocalSlotMirrorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 4, 1), ).setIndexNames((0, "HUAWEI-MIRROR-MIB", "hwLocalSlotNo"))
if mibBuilder.loadTexts: hwLocalSlotMirrorEntry.setStatus('current')
if mibBuilder.loadTexts: hwLocalSlotMirrorEntry.setDescription(' The hwLocalFlowMirrorEntry lists local mirror characters. ')
hwLocalSlotNo = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)))
if mibBuilder.loadTexts: hwLocalSlotNo.setStatus('current')
if mibBuilder.loadTexts: hwLocalSlotNo.setDescription('Slot number of a board.')
hwSlotObserveIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSlotObserveIndex.setStatus('current')
if mibBuilder.loadTexts: hwSlotObserveIndex.setDescription('Indicates the index of the observing port.')
hwLocalSlotMirrorRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 4, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLocalSlotMirrorRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwLocalSlotMirrorRowStatus.setDescription(' Row status. The value ranges from 1 to 6 but usually 4 and 6 are used. createAndGo[4] - create a row. destroy[6] -delete a row. ')
hwPortMirrorInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 5), )
if mibBuilder.loadTexts: hwPortMirrorInfoTable.setStatus('current')
if mibBuilder.loadTexts: hwPortMirrorInfoTable.setDescription(' The hwPortMirrorInfoTable lists local and remote mirror characters. ')
hwPortMirrorInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 5, 1), ).setIndexNames((0, "HUAWEI-MIRROR-MIB", "hwMirrorPortIndex"))
if mibBuilder.loadTexts: hwPortMirrorInfoEntry.setStatus('current')
if mibBuilder.loadTexts: hwPortMirrorInfoEntry.setDescription(' The hwPortMirrorInfoEntry lists local and remote mirror characters. ')
hwMirrorPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 5, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hwMirrorPortIndex.setStatus('current')
if mibBuilder.loadTexts: hwMirrorPortIndex.setDescription('Port index of the mirroring port.')
hwMirrorType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("remote", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMirrorType.setStatus('current')
if mibBuilder.loadTexts: hwMirrorType.setDescription('Mirroring type: local or remote1: local 2: remote.')
hwMirrorCar = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(100, 2500000), ))).setUnits('Kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMirrorCar.setStatus('current')
if mibBuilder.loadTexts: hwMirrorCar.setDescription('CAR (CIR) of mirrored packets, expressed in thousand bits per second ')
hwMirrorClass = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("port", 1), ("policy", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMirrorClass.setStatus('current')
if mibBuilder.loadTexts: hwMirrorClass.setDescription('Type: port/policy1: port 2: policy.')
hwMirrorBearing = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inbound", 1), ("outbound", 2), ("inout", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMirrorBearing.setStatus('current')
if mibBuilder.loadTexts: hwMirrorBearing.setDescription(' Mirroring direction: inbound(1), outbound(2), and in-out(3). When the direction is in-out, commands for both inbound and outbound configurations are required. ')
hwMirrorCpuPacketFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 5, 1, 6), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMirrorCpuPacketFlag.setStatus('current')
if mibBuilder.loadTexts: hwMirrorCpuPacketFlag.setDescription(' Indicates whether the packets sent to the CPU need to be mirrored. True: CPU packets are forwarded; False: CPU packets are not forwarded. ')
hwMirrorWithLinkLayerHeader = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 5, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1)).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMirrorWithLinkLayerHeader.setStatus('current')
if mibBuilder.loadTexts: hwMirrorWithLinkLayerHeader.setDescription(' Same interworking attribute. 1: different interworking, mirroring packets at and above the IP layer. 0: same interworking, mirroring packets at and above Layer 2. Default value: 1. ')
hwRemoteMirrorInstanceName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 5, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwRemoteMirrorInstanceName.setStatus('current')
if mibBuilder.loadTexts: hwRemoteMirrorInstanceName.setDescription('mirror instance name. Max 31 characters.')
hwRemoteMirror = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2))
hwRemoteObserveTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 1), )
if mibBuilder.loadTexts: hwRemoteObserveTable.setStatus('current')
if mibBuilder.loadTexts: hwRemoteObserveTable.setDescription(' The hwRemoteObserveTable lists remote mirror characters. ')
hwRemoteObserveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 1, 1), ).setIndexNames((0, "HUAWEI-MIRROR-MIB", "hwRemoteObservePort"))
if mibBuilder.loadTexts: hwRemoteObserveEntry.setStatus('current')
if mibBuilder.loadTexts: hwRemoteObserveEntry.setDescription(' The hwLocalPortMirrorInfoEntry lists local mirror characters. ')
hwRemoteObservePort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hwRemoteObservePort.setStatus('current')
if mibBuilder.loadTexts: hwRemoteObservePort.setDescription(' Port ifindex of the observing port. ')
hwRemoteIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwRemoteIdentifier.setStatus('current')
if mibBuilder.loadTexts: hwRemoteIdentifier.setDescription(' Mirror Identifier. ')
hwRemoteDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwRemoteDescription.setStatus('current')
if mibBuilder.loadTexts: hwRemoteDescription.setDescription(' Description of the observing port. ')
hwRemoteObserveWithLinkLayerHeader = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwRemoteObserveWithLinkLayerHeader.setStatus('current')
if mibBuilder.loadTexts: hwRemoteObserveWithLinkLayerHeader.setDescription(' Same interworking attribute. 1: different interworking, mirroring packets at and above the IP layer. 0: same interworking, mirroring packets at and above Layer 2. Default value: 1. ')
hwRemoteObserveRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwRemoteObserveRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwRemoteObserveRowStatus.setDescription(' Row status. The value ranges from 1 to 6 but usually 4 and 6 are used. createAndGo[4] - create a row. destroy[6] -delete a row. ')
hwRemotePortMirrorTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 2), )
if mibBuilder.loadTexts: hwRemotePortMirrorTable.setStatus('current')
if mibBuilder.loadTexts: hwRemotePortMirrorTable.setDescription(' The hwRemotePortMirrorTable lists remote mirror characters. ')
hwRemotePortMirrorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 2, 1), ).setIndexNames((0, "HUAWEI-MIRROR-MIB", "hwRemoteMirrorPort"))
if mibBuilder.loadTexts: hwRemotePortMirrorEntry.setStatus('current')
if mibBuilder.loadTexts: hwRemotePortMirrorEntry.setDescription(' The hwRemotePortMirrorTable lists local mirror characters. ')
hwRemoteMirrorPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hwRemoteMirrorPort.setStatus('current')
if mibBuilder.loadTexts: hwRemoteMirrorPort.setDescription(' Port index of the mirroring port. ')
hwRemoteMirrorBearing = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inbound", 1), ("outbound", 2), ("inout", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwRemoteMirrorBearing.setStatus('current')
if mibBuilder.loadTexts: hwRemoteMirrorBearing.setDescription(' Mirroring direction: inbound(1), outbound(2), and in-out(3). When the direction is in-out, commands for both inbound and outbound configurations are required. ')
hwRemoteCpuPacketFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 2, 1, 3), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwRemoteCpuPacketFlag.setStatus('current')
if mibBuilder.loadTexts: hwRemoteCpuPacketFlag.setDescription(' Indicates whether the packets sent to the CPU need to be mirrored. True: CPU packets are forwarded; False: CPU packets are not forwarded. ')
hwPortMirrorInstanceName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwPortMirrorInstanceName.setStatus('current')
if mibBuilder.loadTexts: hwPortMirrorInstanceName.setDescription(' Name of the mirroring instance. It must already exist in the MIB table. ')
hwRemotePortMirrorCar = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(100, 2500000), ))).setUnits('Kbps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwRemotePortMirrorCar.setStatus('current')
if mibBuilder.loadTexts: hwRemotePortMirrorCar.setDescription(' CAR (CIR) of mirrored packets, expressed in thousand bits per second by default, CAR is not performed for mirrored packets. ')
hwRemotePortMirrorRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwRemotePortMirrorRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwRemotePortMirrorRowStatus.setDescription(' Row status. The value ranges from 1 to 6 but usually 4 and 6 are used. createAndGo[4] - create a row. destroy[6] -delete a row. ')
hwRemoteFlowMirrorTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 3), )
if mibBuilder.loadTexts: hwRemoteFlowMirrorTable.setStatus('current')
if mibBuilder.loadTexts: hwRemoteFlowMirrorTable.setDescription(' The hwRemoteFlowMirrorTable lists remote mirror characters. ')
hwRemoteFlowMirrorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 3, 1), ).setIndexNames((0, "HUAWEI-MIRROR-MIB", "hwRemoteBehaviorName"))
if mibBuilder.loadTexts: hwRemoteFlowMirrorEntry.setStatus('current')
if mibBuilder.loadTexts: hwRemoteFlowMirrorEntry.setDescription(' The hwRemoteFlowMirrorEntry lists local mirror characters. ')
hwRemoteBehaviorName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 3, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31)))
if mibBuilder.loadTexts: hwRemoteBehaviorName.setStatus('current')
if mibBuilder.loadTexts: hwRemoteBehaviorName.setDescription(' Name of the traffic behavior. ')
hwFlowMirrorInstanceName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwFlowMirrorInstanceName.setStatus('current')
if mibBuilder.loadTexts: hwFlowMirrorInstanceName.setDescription(' Name of the mirroring instance. ')
hwRemoteFlowMirrorCar = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(100, 2500000), ))).setUnits('Kbps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwRemoteFlowMirrorCar.setStatus('current')
if mibBuilder.loadTexts: hwRemoteFlowMirrorCar.setDescription(' CAR (Committed Access Rate) setting of the mirror flow. The value indicates the CIR(Committed information rate) measured in kbps. ')
hwRemoteFlowMirrorRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwRemoteFlowMirrorRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwRemoteFlowMirrorRowStatus.setDescription(' Row status. The value ranges from 1 to 6 but usually 4 and 6 are used. createAndGo[4] - create a row. destroy[6] -delete a row. ')
hwRemoteMirrorInstanceTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 4), )
if mibBuilder.loadTexts: hwRemoteMirrorInstanceTable.setStatus('current')
if mibBuilder.loadTexts: hwRemoteMirrorInstanceTable.setDescription(' The hwRemoteMirrorInstanceTable lists remote mirror characters. ')
hwRemoteMirrorInstanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 4, 1), ).setIndexNames((0, "HUAWEI-MIRROR-MIB", "hwMirrorInstanceName"))
if mibBuilder.loadTexts: hwRemoteMirrorInstanceEntry.setStatus('current')
if mibBuilder.loadTexts: hwRemoteMirrorInstanceEntry.setDescription(' The hwRemoteMirrorInstanceEntry lists mirror instance characters. ')
hwMirrorInstanceName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 4, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31)))
if mibBuilder.loadTexts: hwMirrorInstanceName.setStatus('current')
if mibBuilder.loadTexts: hwMirrorInstanceName.setDescription(' Mirroring instance name. Max 31 characters ')
hwRemoteObservePortIp = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 4, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwRemoteObservePortIp.setStatus('current')
if mibBuilder.loadTexts: hwRemoteObservePortIp.setDescription(' Remote mirror destination.')
hwRemoteMirrorIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 64), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwRemoteMirrorIdentifier.setStatus('current')
if mibBuilder.loadTexts: hwRemoteMirrorIdentifier.setDescription(' Mirror identifier. ')
hwRemoteMirrorWithLinkLayerHeader = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwRemoteMirrorWithLinkLayerHeader.setStatus('current')
if mibBuilder.loadTexts: hwRemoteMirrorWithLinkLayerHeader.setDescription(' Same interworking attribute. 1: different interworking, mirroring packets at and above the IP layer. 0: same interworking, mirroring packets at and above Layer 2. Default value: 1. ')
hwMirrorFlowClass = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("be", 0), ("af1", 1), ("af2", 2), ("af3", 3), ("af4", 4), ("ef", 5), ("cs6", 6), ("cs7", 7)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMirrorFlowClass.setStatus('current')
if mibBuilder.loadTexts: hwMirrorFlowClass.setDescription(' Type of mirrored flows. The value of 0 to 7 corresponds to <be,af1,af2,af3,af4,ef,cs6,cs7> respectively. be (0), af1 (1), af2 (2), af3 (3), af4 (4), ef (5), cs6 (6), cs7 (7) ')
hwMirrorSliceSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(64, 9600), ))).setUnits('Byte').setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMirrorSliceSize.setStatus('current')
if mibBuilder.loadTexts: hwMirrorSliceSize.setDescription(' Number of bytes of intercepted packets, expressed in bytes. The value of size ranges from 64 to 9600. ')
hwMirrorTunnelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMirrorTunnelIndex.setStatus('current')
if mibBuilder.loadTexts: hwMirrorTunnelIndex.setDescription(' Index of the tunnel that uniquely identifies the tunnel. ')
hwMirrorTunnelType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("lspTunnel", 1), ("teTunnel", 2), ("greTunnel", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMirrorTunnelType.setStatus('current')
if mibBuilder.loadTexts: hwMirrorTunnelType.setDescription(' Type of the tunnel: 1: LSP tunnel 2: TE tunnel 3: GRE tunnel ')
hwMirrorTunnelStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 4, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMirrorTunnelStatus.setStatus('current')
if mibBuilder.loadTexts: hwMirrorTunnelStatus.setDescription(' status of tunnel 0:DOWN 1:UP ')
hwMirrorTunnelPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 4, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 19))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMirrorTunnelPolicy.setStatus('current')
if mibBuilder.loadTexts: hwMirrorTunnelPolicy.setDescription(' Tunnel policy name. Max 19 characters ')
hwMirrorInstanceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 4, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMirrorInstanceRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwMirrorInstanceRowStatus.setDescription(' Row status. The value ranges from 1 to 6 but usually 4 and 6 are used. createAndGo[4] - create a row. destroy[6] -delete a row. ')
hwMirrorConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 162, 11))
hwMirrorCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 162, 11, 1))
hwMirrorCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 162, 11, 1, 1)).setObjects(("HUAWEI-MIRROR-MIB", "hwLocalObserveGroup"), ("HUAWEI-MIRROR-MIB", "hwLocalPortMirrorGroup"), ("HUAWEI-MIRROR-MIB", "hwLocalFlowMirrorGroup"), ("HUAWEI-MIRROR-MIB", "hwLocalSlotMirrorGroup"), ("HUAWEI-MIRROR-MIB", "hwLocalPortMirrorInfoGroup"), ("HUAWEI-MIRROR-MIB", "hwRemoteObserveGroup"), ("HUAWEI-MIRROR-MIB", "hwRemotePortMirrorGroup"), ("HUAWEI-MIRROR-MIB", "hwRemoteFlowMirrorGroup"), ("HUAWEI-MIRROR-MIB", "hwRemoteMirrorInstanceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwMirrorCompliance = hwMirrorCompliance.setStatus('current')
if mibBuilder.loadTexts: hwMirrorCompliance.setDescription('The compliance statement for systems supporting the HUAWEI-SECURITY-MIB.')
hwBaseMirrorGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 162, 11, 2))
hwLocalObserveGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 162, 11, 2, 1)).setObjects(("HUAWEI-MIRROR-MIB", "hwLocalObserveIndex"), ("HUAWEI-MIRROR-MIB", "hwLocalObserveWithLinkLayerHeader"), ("HUAWEI-MIRROR-MIB", "hwLocalObserveRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwLocalObserveGroup = hwLocalObserveGroup.setStatus('current')
if mibBuilder.loadTexts: hwLocalObserveGroup.setDescription('The group specifies local observing port.')
hwLocalPortMirrorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 162, 11, 2, 2)).setObjects(("HUAWEI-MIRROR-MIB", "hwLocalMirrorBearing"), ("HUAWEI-MIRROR-MIB", "hwLocalCpuPacketFlag"), ("HUAWEI-MIRROR-MIB", "hwLocalPortMirrorCar"), ("HUAWEI-MIRROR-MIB", "hwLocalPortMirrorRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwLocalPortMirrorGroup = hwLocalPortMirrorGroup.setStatus('current')
if mibBuilder.loadTexts: hwLocalPortMirrorGroup.setDescription('The group specifies local mirroring port.')
hwLocalFlowMirrorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 162, 11, 2, 3)).setObjects(("HUAWEI-MIRROR-MIB", "hwLocalFlowMirrorEnable"), ("HUAWEI-MIRROR-MIB", "hwLocalFlowMirrorCar"), ("HUAWEI-MIRROR-MIB", "hwLocalFlowMirrorRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwLocalFlowMirrorGroup = hwLocalFlowMirrorGroup.setStatus('current')
if mibBuilder.loadTexts: hwLocalFlowMirrorGroup.setDescription('The group specifies traffic behavior for local mirroring.')
hwLocalSlotMirrorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 162, 11, 2, 4)).setObjects(("HUAWEI-MIRROR-MIB", "hwSlotObserveIndex"), ("HUAWEI-MIRROR-MIB", "hwLocalSlotMirrorRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwLocalSlotMirrorGroup = hwLocalSlotMirrorGroup.setStatus('current')
if mibBuilder.loadTexts: hwLocalSlotMirrorGroup.setDescription('The group specifies local observing port for slot.')
hwLocalPortMirrorInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 162, 11, 2, 5)).setObjects(("HUAWEI-MIRROR-MIB", "hwMirrorType"), ("HUAWEI-MIRROR-MIB", "hwMirrorCar"), ("HUAWEI-MIRROR-MIB", "hwMirrorClass"), ("HUAWEI-MIRROR-MIB", "hwMirrorBearing"), ("HUAWEI-MIRROR-MIB", "hwMirrorCpuPacketFlag"), ("HUAWEI-MIRROR-MIB", "hwMirrorWithLinkLayerHeader"), ("HUAWEI-MIRROR-MIB", "hwRemoteMirrorInstanceName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwLocalPortMirrorInfoGroup = hwLocalPortMirrorInfoGroup.setStatus('current')
if mibBuilder.loadTexts: hwLocalPortMirrorInfoGroup.setDescription('The group querys configuration of port-mirroring interfaces.')
hwRemoteObserveGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 162, 11, 2, 6)).setObjects(("HUAWEI-MIRROR-MIB", "hwRemoteIdentifier"), ("HUAWEI-MIRROR-MIB", "hwRemoteDescription"), ("HUAWEI-MIRROR-MIB", "hwRemoteObserveWithLinkLayerHeader"), ("HUAWEI-MIRROR-MIB", "hwRemoteObserveRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwRemoteObserveGroup = hwRemoteObserveGroup.setStatus('current')
if mibBuilder.loadTexts: hwRemoteObserveGroup.setDescription('The group specifies remote observing port.')
hwRemotePortMirrorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 162, 11, 2, 7)).setObjects(("HUAWEI-MIRROR-MIB", "hwRemoteMirrorBearing"), ("HUAWEI-MIRROR-MIB", "hwRemoteCpuPacketFlag"), ("HUAWEI-MIRROR-MIB", "hwPortMirrorInstanceName"), ("HUAWEI-MIRROR-MIB", "hwRemotePortMirrorCar"), ("HUAWEI-MIRROR-MIB", "hwRemotePortMirrorRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwRemotePortMirrorGroup = hwRemotePortMirrorGroup.setStatus('current')
if mibBuilder.loadTexts: hwRemotePortMirrorGroup.setDescription('The group specifies remote mirroring port.')
hwRemoteFlowMirrorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 162, 11, 2, 8)).setObjects(("HUAWEI-MIRROR-MIB", "hwFlowMirrorInstanceName"), ("HUAWEI-MIRROR-MIB", "hwRemoteFlowMirrorCar"), ("HUAWEI-MIRROR-MIB", "hwRemoteFlowMirrorRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwRemoteFlowMirrorGroup = hwRemoteFlowMirrorGroup.setStatus('current')
if mibBuilder.loadTexts: hwRemoteFlowMirrorGroup.setDescription('The group specifies traffic behavior for remote mirroring.')
hwRemoteMirrorInstanceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 162, 11, 2, 9)).setObjects(("HUAWEI-MIRROR-MIB", "hwRemoteObservePortIp"), ("HUAWEI-MIRROR-MIB", "hwRemoteMirrorIdentifier"), ("HUAWEI-MIRROR-MIB", "hwRemoteMirrorWithLinkLayerHeader"), ("HUAWEI-MIRROR-MIB", "hwMirrorFlowClass"), ("HUAWEI-MIRROR-MIB", "hwMirrorSliceSize"), ("HUAWEI-MIRROR-MIB", "hwMirrorTunnelIndex"), ("HUAWEI-MIRROR-MIB", "hwMirrorTunnelType"), ("HUAWEI-MIRROR-MIB", "hwMirrorTunnelStatus"), ("HUAWEI-MIRROR-MIB", "hwMirrorInstanceRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwRemoteMirrorInstanceGroup = hwRemoteMirrorInstanceGroup.setStatus('current')
if mibBuilder.loadTexts: hwRemoteMirrorInstanceGroup.setDescription('The group specifies mirror instance.')
mibBuilder.exportSymbols("HUAWEI-MIRROR-MIB", hwRemoteMirrorInstanceName=hwRemoteMirrorInstanceName, hwMirrorTunnelPolicy=hwMirrorTunnelPolicy, hwFlowMirrorInstanceName=hwFlowMirrorInstanceName, hwMirrorType=hwMirrorType, hwLocalFlowMirrorGroup=hwLocalFlowMirrorGroup, hwMirrorCpuPacketFlag=hwMirrorCpuPacketFlag, hwMirrorPortIndex=hwMirrorPortIndex, hwMirrorMIB=hwMirrorMIB, hwMirrorTunnelType=hwMirrorTunnelType, hwRemotePortMirrorEntry=hwRemotePortMirrorEntry, hwRemoteMirrorWithLinkLayerHeader=hwRemoteMirrorWithLinkLayerHeader, hwLocalPortMirrorEntry=hwLocalPortMirrorEntry, hwLocalSlotMirrorRowStatus=hwLocalSlotMirrorRowStatus, hwLocalBehaviorName=hwLocalBehaviorName, hwRemoteObserveGroup=hwRemoteObserveGroup, PYSNMP_MODULE_ID=hwMirrorMIB, hwRemoteMirrorPort=hwRemoteMirrorPort, hwRemoteFlowMirrorTable=hwRemoteFlowMirrorTable, hwLocalPortMirrorInfoGroup=hwLocalPortMirrorInfoGroup, hwMirrorClass=hwMirrorClass, hwSlotObserveIndex=hwSlotObserveIndex, hwLocalPortMirrorRowStatus=hwLocalPortMirrorRowStatus, hwPortMirrorInfoEntry=hwPortMirrorInfoEntry, hwLocalObservePort=hwLocalObservePort, hwRemoteObserveRowStatus=hwRemoteObserveRowStatus, hwPortMirrorInstanceName=hwPortMirrorInstanceName, hwRemoteMirrorIdentifier=hwRemoteMirrorIdentifier, hwRemoteObservePortIp=hwRemoteObservePortIp, hwLocalMirrorBearing=hwLocalMirrorBearing, hwLocalPortMirrorCar=hwLocalPortMirrorCar, hwLocalFlowMirrorEnable=hwLocalFlowMirrorEnable, hwPortMirrorInfoTable=hwPortMirrorInfoTable, hwLocalMirrorPort=hwLocalMirrorPort, hwLocalObserveEntry=hwLocalObserveEntry, hwRemoteMirrorInstanceTable=hwRemoteMirrorInstanceTable, hwMirrorConformance=hwMirrorConformance, hwMirrorFlowClass=hwMirrorFlowClass, hwRemoteMirrorBearing=hwRemoteMirrorBearing, hwLocalSlotMirrorGroup=hwLocalSlotMirrorGroup, hwLocalObserveIndex=hwLocalObserveIndex, hwLocalFlowMirrorEntry=hwLocalFlowMirrorEntry, hwMirrorTunnelStatus=hwMirrorTunnelStatus, hwRemotePortMirrorTable=hwRemotePortMirrorTable, hwMirrorMIBObjects=hwMirrorMIBObjects, hwLocalMirror=hwLocalMirror, hwRemoteMirrorInstanceGroup=hwRemoteMirrorInstanceGroup, hwMirrorBearing=hwMirrorBearing, hwLocalCpuPacketFlag=hwLocalCpuPacketFlag, hwRemoteObservePort=hwRemoteObservePort, hwLocalPortMirrorTable=hwLocalPortMirrorTable, hwLocalPortMirrorGroup=hwLocalPortMirrorGroup, hwMirrorSliceSize=hwMirrorSliceSize, hwRemotePortMirrorGroup=hwRemotePortMirrorGroup, hwLocalFlowMirrorRowStatus=hwLocalFlowMirrorRowStatus, hwMirrorTunnelIndex=hwMirrorTunnelIndex, hwLocalObserveRowStatus=hwLocalObserveRowStatus, hwRemoteObserveEntry=hwRemoteObserveEntry, hwRemoteFlowMirrorCar=hwRemoteFlowMirrorCar, hwLocalSlotMirrorTable=hwLocalSlotMirrorTable, hwRemoteMirrorInstanceEntry=hwRemoteMirrorInstanceEntry, hwLocalSlotNo=hwLocalSlotNo, hwLocalFlowMirrorCar=hwLocalFlowMirrorCar, hwRemoteFlowMirrorGroup=hwRemoteFlowMirrorGroup, hwMirrorInstanceRowStatus=hwMirrorInstanceRowStatus, hwRemoteDescription=hwRemoteDescription, hwRemoteCpuPacketFlag=hwRemoteCpuPacketFlag, hwLocalObserveGroup=hwLocalObserveGroup, hwBaseMirrorGroup=hwBaseMirrorGroup, hwMirrorCompliance=hwMirrorCompliance, hwRemotePortMirrorCar=hwRemotePortMirrorCar, hwLocalObserveTable=hwLocalObserveTable, hwRemoteMirror=hwRemoteMirror, hwRemoteFlowMirrorEntry=hwRemoteFlowMirrorEntry, hwMirrorWithLinkLayerHeader=hwMirrorWithLinkLayerHeader, hwRemoteIdentifier=hwRemoteIdentifier, hwMirrorCompliances=hwMirrorCompliances, hwRemoteObserveWithLinkLayerHeader=hwRemoteObserveWithLinkLayerHeader, hwRemotePortMirrorRowStatus=hwRemotePortMirrorRowStatus, hwLocalObserveWithLinkLayerHeader=hwLocalObserveWithLinkLayerHeader, hwMirrorInstanceName=hwMirrorInstanceName, hwLocalFlowMirrorTable=hwLocalFlowMirrorTable, hwMirrorCar=hwMirrorCar, hwRemoteBehaviorName=hwRemoteBehaviorName, hwLocalSlotMirrorEntry=hwLocalSlotMirrorEntry, hwRemoteFlowMirrorRowStatus=hwRemoteFlowMirrorRowStatus, hwRemoteObserveTable=hwRemoteObserveTable)
