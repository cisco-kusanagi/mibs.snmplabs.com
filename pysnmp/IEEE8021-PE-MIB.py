#
# PySNMP MIB module IEEE8021-PE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IEEE8021-PE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:41:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ieee802dot1mibs, IEEE8021BridgePortNumberOrZero, IEEE8021BridgePortNumber, IEEE8021PbbComponentIdentifier = mibBuilder.importSymbols("IEEE8021-TC-MIB", "ieee802dot1mibs", "IEEE8021BridgePortNumberOrZero", "IEEE8021BridgePortNumber", "IEEE8021PbbComponentIdentifier")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, ModuleIdentity, Counter64, Integer32, iso, Unsigned32, TimeTicks, NotificationType, Counter32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "Counter64", "Integer32", "iso", "Unsigned32", "TimeTicks", "NotificationType", "Counter32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "IpAddress")
MacAddress, TimeStamp, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TimeStamp", "TruthValue", "TextualConvention", "DisplayString")
ieee8021BridgePEMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 25))
ieee8021BridgePEMib.setRevisions(('2012-01-22 00:00',))
if mibBuilder.loadTexts: ieee8021BridgePEMib.setLastUpdated('201201220000Z')
if mibBuilder.loadTexts: ieee8021BridgePEMib.setOrganization('IEEE 802.1 Working Group')
ieee8021BridgePENotifications = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 25, 1))
ieee8021BridgePEObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 25, 2))
ieee8021BridgePEConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 25, 3))
class IEEE802BridgePEEChannelIDTC(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4194302)

class IEEE802BridgePETrafficClassValueTC(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 7)

class IEEE802BridgePETrafficSelectionAlgorithmTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 255))
    namedValues = NamedValues(("tsaStrictPriority", 0), ("tsaCreditBasedShaper", 1), ("tsaEnhancedTransmission", 2), ("tsaVendorSpecific", 255))

class IEEE802BridgePETrafficClassBandwidthValue(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 100)

ieee8021BridgePEPortTable = MibTable((1, 3, 111, 2, 802, 1, 1, 25, 2, 1), )
if mibBuilder.loadTexts: ieee8021BridgePEPortTable.setStatus('current')
ieee8021BridgePEPortEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1), ).setIndexNames((0, "IEEE8021-PE-MIB", "ieee8021BridgePEPortComponentId"), (0, "IEEE8021-PE-MIB", "ieee8021BridgePEPort"), (0, "IEEE8021-PE-MIB", "ieee8021BridgePEPortType"))
if mibBuilder.loadTexts: ieee8021BridgePEPortEntry.setStatus('current')
ieee8021BridgePEPortComponentId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 1), IEEE8021PbbComponentIdentifier())
if mibBuilder.loadTexts: ieee8021BridgePEPortComponentId.setStatus('current')
ieee8021BridgePEPort = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 2), IEEE8021BridgePortNumber())
if mibBuilder.loadTexts: ieee8021BridgePEPort.setStatus('current')
ieee8021BridgePEPortType = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("pepCascade", 1), ("pepUpstream", 2), ("pepExtended", 3))))
if mibBuilder.loadTexts: ieee8021BridgePEPortType.setStatus('current')
ieee8021BridgePEPortUpstreamCSPAddress = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePEPortUpstreamCSPAddress.setStatus('current')
ieee8021BridgePEPortEcid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 5), IEEE802BridgePEEChannelIDTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePEPortEcid.setStatus('current')
ieee8021BridgePEPortNumber = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 6), IEEE8021BridgePortNumberOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePEPortNumber.setStatus('current')
ieee8021BridgePECounterDiscontinuityTime = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePECounterDiscontinuityTime.setStatus('current')
ieee8021BridgePEPortRxrqErrorsBridge = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 8), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePEPortRxrqErrorsBridge.setStatus('current')
ieee8021BridgePEPortRxrspErrorsBridge = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 9), Counter64()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePEPortRxrspErrorsBridge.setStatus('current')
ieee8021BridgePEPortRxrqErrorsPE = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 10), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePEPortRxrqErrorsPE.setStatus('current')
ieee8021BridgePEPortRxrspErrorsPE = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 11), Counter64()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePEPortRxrspErrorsPE.setStatus('current')
ieee8021BridgePEPCP = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 12), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePEPCP.setStatus('current')
ieee8021BridgePEROW = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 13), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePEROW.setStatus('current')
ieee8021BridgePEDEI = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 14), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePEDEI.setStatus('current')
ieee8021BridgePECN = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 15), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePECN.setStatus('current')
ieee8021BridgePEPFC = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 16), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePEPFC.setStatus('current')
ieee8021BridgePEExtPortEChannelsSupported = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 17), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1048575))).setUnits('E-channels').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePEExtPortEChannelsSupported.setStatus('current')
ieee8021BridgePERemoteRepEChannelsSupported = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 18), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 3145727))).setUnits('E-channels').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePERemoteRepEChannelsSupported.setStatus('current')
ieee8021BridgePETCsSupported = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 19), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setUnits('traffic classes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePETCsSupported.setStatus('current')
ieee8021BridgePEUtVLANsSupported = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 20), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setUnits('VLANs').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePEUtVLANsSupported.setStatus('current')
ieee8021BridgePERemoteReplicationTable = MibTable((1, 3, 111, 2, 802, 1, 1, 25, 2, 2), )
if mibBuilder.loadTexts: ieee8021BridgePERemoteReplicationTable.setStatus('current')
ieee8021BridgePERemoteReplicationEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 25, 2, 2, 1), ).setIndexNames((0, "IEEE8021-PE-MIB", "ieee8021BridgePEPortComponentId"), (0, "IEEE8021-PE-MIB", "ieee8021BridgePERREcid"))
if mibBuilder.loadTexts: ieee8021BridgePERemoteReplicationEntry.setStatus('current')
ieee8021BridgePERREcid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 2, 1, 1), IEEE802BridgePEEChannelIDTC())
if mibBuilder.loadTexts: ieee8021BridgePERREcid.setStatus('current')
ieee8021BridgePERRPortMap = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 2, 1, 2), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePERRPortMap.setStatus('current')
ieee8021BridgePEETSTable = MibTable((1, 3, 111, 2, 802, 1, 1, 25, 2, 3), )
if mibBuilder.loadTexts: ieee8021BridgePEETSTable.setStatus('current')
ieee8021BridgePEETSEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 25, 2, 3, 1), ).setIndexNames((0, "IEEE8021-PE-MIB", "ieee8021BridgePEPortComponentId"), (0, "IEEE8021-PE-MIB", "ieee8021BridgePEPort"), (0, "IEEE8021-PE-MIB", "ieee8021BridgePEETSTrafficClass"))
if mibBuilder.loadTexts: ieee8021BridgePEETSEntry.setStatus('current')
ieee8021BridgePEETSTrafficClass = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 3, 1, 1), IEEE802BridgePETrafficClassValueTC())
if mibBuilder.loadTexts: ieee8021BridgePEETSTrafficClass.setStatus('current')
ieee8021BridgePEETSTrafficSelectionAlgorthm = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 3, 1, 2), IEEE802BridgePETrafficSelectionAlgorithmTC()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021BridgePEETSTrafficSelectionAlgorthm.setStatus('current')
ieee8021BridgePEETSBandwidth = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 3, 1, 3), IEEE802BridgePETrafficClassBandwidthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021BridgePEETSBandwidth.setStatus('current')
ieee8021BridgePEGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 25, 3, 1))
ieee8021BridgePECompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 25, 3, 2))
ieee8021BridgePEGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 25, 3, 1, 1)).setObjects(("IEEE8021-PE-MIB", "ieee8021BridgePEPortUpstreamCSPAddress"), ("IEEE8021-PE-MIB", "ieee8021BridgePEPortEcid"), ("IEEE8021-PE-MIB", "ieee8021BridgePEPortNumber"), ("IEEE8021-PE-MIB", "ieee8021BridgePECounterDiscontinuityTime"), ("IEEE8021-PE-MIB", "ieee8021BridgePEPortRxrqErrorsBridge"), ("IEEE8021-PE-MIB", "ieee8021BridgePEPortRxrspErrorsBridge"), ("IEEE8021-PE-MIB", "ieee8021BridgePEPortRxrqErrorsPE"), ("IEEE8021-PE-MIB", "ieee8021BridgePEPortRxrspErrorsPE"), ("IEEE8021-PE-MIB", "ieee8021BridgePEPCP"), ("IEEE8021-PE-MIB", "ieee8021BridgePEROW"), ("IEEE8021-PE-MIB", "ieee8021BridgePEDEI"), ("IEEE8021-PE-MIB", "ieee8021BridgePECN"), ("IEEE8021-PE-MIB", "ieee8021BridgePEPFC"), ("IEEE8021-PE-MIB", "ieee8021BridgePEExtPortEChannelsSupported"), ("IEEE8021-PE-MIB", "ieee8021BridgePERemoteRepEChannelsSupported"), ("IEEE8021-PE-MIB", "ieee8021BridgePETCsSupported"), ("IEEE8021-PE-MIB", "ieee8021BridgePEUtVLANsSupported"), ("IEEE8021-PE-MIB", "ieee8021BridgePERRPortMap"), ("IEEE8021-PE-MIB", "ieee8021BridgePEETSTrafficSelectionAlgorthm"), ("IEEE8021-PE-MIB", "ieee8021BridgePEETSBandwidth"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021BridgePEGroup = ieee8021BridgePEGroup.setStatus('current')
ieee8021BridgePECompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 25, 3, 2, 1)).setObjects(("IEEE8021-PE-MIB", "ieee8021BridgePEGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021BridgePECompliance = ieee8021BridgePECompliance.setStatus('current')
mibBuilder.exportSymbols("IEEE8021-PE-MIB", ieee8021BridgePEPCP=ieee8021BridgePEPCP, ieee8021BridgePEPortRxrqErrorsBridge=ieee8021BridgePEPortRxrqErrorsBridge, ieee8021BridgePEGroup=ieee8021BridgePEGroup, ieee8021BridgePECN=ieee8021BridgePECN, ieee8021BridgePEGroups=ieee8021BridgePEGroups, ieee8021BridgePEPortRxrspErrorsBridge=ieee8021BridgePEPortRxrspErrorsBridge, ieee8021BridgePETCsSupported=ieee8021BridgePETCsSupported, ieee8021BridgePEROW=ieee8021BridgePEROW, ieee8021BridgePEPortTable=ieee8021BridgePEPortTable, ieee8021BridgePEExtPortEChannelsSupported=ieee8021BridgePEExtPortEChannelsSupported, PYSNMP_MODULE_ID=ieee8021BridgePEMib, ieee8021BridgePEPortEntry=ieee8021BridgePEPortEntry, ieee8021BridgePECompliance=ieee8021BridgePECompliance, ieee8021BridgePEPortEcid=ieee8021BridgePEPortEcid, ieee8021BridgePEConformance=ieee8021BridgePEConformance, ieee8021BridgePEDEI=ieee8021BridgePEDEI, ieee8021BridgePERemoteReplicationTable=ieee8021BridgePERemoteReplicationTable, ieee8021BridgePECompliances=ieee8021BridgePECompliances, ieee8021BridgePERRPortMap=ieee8021BridgePERRPortMap, ieee8021BridgePECounterDiscontinuityTime=ieee8021BridgePECounterDiscontinuityTime, ieee8021BridgePEMib=ieee8021BridgePEMib, IEEE802BridgePETrafficClassBandwidthValue=IEEE802BridgePETrafficClassBandwidthValue, IEEE802BridgePETrafficSelectionAlgorithmTC=IEEE802BridgePETrafficSelectionAlgorithmTC, ieee8021BridgePEPortNumber=ieee8021BridgePEPortNumber, ieee8021BridgePEPort=ieee8021BridgePEPort, ieee8021BridgePERemoteRepEChannelsSupported=ieee8021BridgePERemoteRepEChannelsSupported, ieee8021BridgePEPortUpstreamCSPAddress=ieee8021BridgePEPortUpstreamCSPAddress, ieee8021BridgePEPortType=ieee8021BridgePEPortType, IEEE802BridgePEEChannelIDTC=IEEE802BridgePEEChannelIDTC, ieee8021BridgePENotifications=ieee8021BridgePENotifications, ieee8021BridgePEPFC=ieee8021BridgePEPFC, ieee8021BridgePEETSEntry=ieee8021BridgePEETSEntry, ieee8021BridgePEETSBandwidth=ieee8021BridgePEETSBandwidth, ieee8021BridgePEUtVLANsSupported=ieee8021BridgePEUtVLANsSupported, ieee8021BridgePEObjects=ieee8021BridgePEObjects, ieee8021BridgePEETSTrafficSelectionAlgorthm=ieee8021BridgePEETSTrafficSelectionAlgorthm, ieee8021BridgePEPortRxrqErrorsPE=ieee8021BridgePEPortRxrqErrorsPE, ieee8021BridgePERemoteReplicationEntry=ieee8021BridgePERemoteReplicationEntry, ieee8021BridgePEETSTable=ieee8021BridgePEETSTable, ieee8021BridgePEETSTrafficClass=ieee8021BridgePEETSTrafficClass, ieee8021BridgePEPortComponentId=ieee8021BridgePEPortComponentId, ieee8021BridgePEPortRxrspErrorsPE=ieee8021BridgePEPortRxrspErrorsPE, IEEE802BridgePETrafficClassValueTC=IEEE802BridgePETrafficClassValueTC, ieee8021BridgePERREcid=ieee8021BridgePERREcid)
