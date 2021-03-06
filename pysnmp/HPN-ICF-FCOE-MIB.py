#
# PySNMP MIB module HPN-ICF-FCOE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-FCOE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:26:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
fcmInstanceIndex, = mibBuilder.importSymbols("FC-MGMT-MIB", "fcmInstanceIndex")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ModuleIdentity, ObjectIdentity, MibIdentifier, Unsigned32, NotificationType, TimeTicks, Counter32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, IpAddress, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "Unsigned32", "NotificationType", "TimeTicks", "Counter32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "IpAddress", "Counter64")
TextualConvention, MacAddress, DisplayString, RowStatus, TruthValue, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString", "RowStatus", "TruthValue", "TimeStamp")
T11FabricIndex, = mibBuilder.importSymbols("T11-TC-MIB", "T11FabricIndex")
hpnicfFCoE = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120))
hpnicfFCoE.setRevisions(('2012-03-28 00:00',))
if mibBuilder.loadTexts: hpnicfFCoE.setLastUpdated('201203280000Z')
if mibBuilder.loadTexts: hpnicfFCoE.setOrganization('')
hpnicfFCoEObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1))
hpnicfFCoEConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1))
class HpnicfFCoEVfcBindType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("interfaceIndex", 1), ("macAddress", 2))

hpnicfFCoECfgTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 1), )
if mibBuilder.loadTexts: hpnicfFCoECfgTable.setStatus('current')
hpnicfFCoECfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 1, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"))
if mibBuilder.loadTexts: hpnicfFCoECfgEntry.setStatus('current')
hpnicfFCoECfgFcmap = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3).clone(hexValue="0EFC00")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfFCoECfgFcmap.setStatus('current')
hpnicfFCoECfgDynamicVfcCreation = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfFCoECfgDynamicVfcCreation.setStatus('current')
hpnicfFCoECfgDefaultFCFPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(128)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfFCoECfgDefaultFCFPriority.setStatus('current')
hpnicfFCoECfgDATov = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 600)).clone(5)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfFCoECfgDATov.setStatus('current')
hpnicfFCoECfgAddressingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("fpma", 1), ("spma", 2), ("fpmaAndSpma", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfFCoECfgAddressingMode.setStatus('current')
hpnicfFCoEVLANTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 2), )
if mibBuilder.loadTexts: hpnicfFCoEVLANTable.setStatus('current')
hpnicfFCoEVLANEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 2, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "HPN-ICF-FCOE-MIB", "hpnicfFCoEVLANIndex"), (0, "HPN-ICF-FCOE-MIB", "hpnicfFCoEFabricIndex"))
if mibBuilder.loadTexts: hpnicfFCoEVLANEntry.setStatus('current')
hpnicfFCoEVLANIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 2, 1, 1), VlanIndex())
if mibBuilder.loadTexts: hpnicfFCoEVLANIndex.setStatus('current')
hpnicfFCoEFabricIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 2, 1, 2), T11FabricIndex())
if mibBuilder.loadTexts: hpnicfFCoEFabricIndex.setStatus('current')
hpnicfFCoEVLANOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFCoEVLANOperState.setStatus('current')
hpnicfFCoEVLANRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfFCoEVLANRowStatus.setStatus('current')
hpnicfFCoEStaticVfcTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 3), )
if mibBuilder.loadTexts: hpnicfFCoEStaticVfcTable.setStatus('current')
hpnicfFCoEStaticVfcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 3, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "HPN-ICF-FCOE-MIB", "hpnicfFCoEStaticVfcIndex"))
if mibBuilder.loadTexts: hpnicfFCoEStaticVfcEntry.setStatus('current')
hpnicfFCoEStaticVfcIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hpnicfFCoEStaticVfcIndex.setStatus('current')
hpnicfFCoEStaticVfcFCFPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(128)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfFCoEStaticVfcFCFPriority.setStatus('current')
hpnicfFCoEStaticVfcBindType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 3, 1, 3), HpnicfFCoEVfcBindType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfFCoEStaticVfcBindType.setStatus('current')
hpnicfFCoEStaticVfcBindIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 3, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfFCoEStaticVfcBindIfIndex.setStatus('current')
hpnicfFCoEStaticVfcBindMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 3, 1, 5), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfFCoEStaticVfcBindMACAddress.setStatus('current')
hpnicfFCoEStaticVfcIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 3, 1, 6), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFCoEStaticVfcIfIndex.setStatus('current')
hpnicfFCoEStaticVfcCreationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 3, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFCoEStaticVfcCreationTime.setStatus('current')
hpnicfFCoEStaticVfcFailureCause = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 3, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFCoEStaticVfcFailureCause.setStatus('current')
hpnicfFCoEStaticVfcRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 3, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfFCoEStaticVfcRowStatus.setStatus('current')
hpnicfFCoEFIPSnoopingTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 4), )
if mibBuilder.loadTexts: hpnicfFCoEFIPSnoopingTable.setStatus('current')
hpnicfFCoEFIPSnoopingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 4, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "HPN-ICF-FCOE-MIB", "hpnicfFCoEFIPSnoopingVLANIndex"))
if mibBuilder.loadTexts: hpnicfFCoEFIPSnoopingEntry.setStatus('current')
hpnicfFCoEFIPSnoopingVLANIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 4, 1, 1), VlanIndex())
if mibBuilder.loadTexts: hpnicfFCoEFIPSnoopingVLANIndex.setStatus('current')
hpnicfFCoEFIPSnoopingEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 4, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfFCoEFIPSnoopingEnable.setStatus('current')
hpnicfFCoEFIPSnoopingFcmap = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 4, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3).clone(hexValue="0EFC00")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfFCoEFIPSnoopingFcmap.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-FCOE-MIB", PYSNMP_MODULE_ID=hpnicfFCoE, hpnicfFCoECfgDefaultFCFPriority=hpnicfFCoECfgDefaultFCFPriority, hpnicfFCoEStaticVfcBindIfIndex=hpnicfFCoEStaticVfcBindIfIndex, hpnicfFCoEVLANOperState=hpnicfFCoEVLANOperState, HpnicfFCoEVfcBindType=HpnicfFCoEVfcBindType, hpnicfFCoEFIPSnoopingVLANIndex=hpnicfFCoEFIPSnoopingVLANIndex, hpnicfFCoEStaticVfcIndex=hpnicfFCoEStaticVfcIndex, hpnicfFCoECfgFcmap=hpnicfFCoECfgFcmap, hpnicfFCoECfgAddressingMode=hpnicfFCoECfgAddressingMode, hpnicfFCoEStaticVfcRowStatus=hpnicfFCoEStaticVfcRowStatus, hpnicfFCoECfgEntry=hpnicfFCoECfgEntry, hpnicfFCoEFIPSnoopingEntry=hpnicfFCoEFIPSnoopingEntry, hpnicfFCoEFIPSnoopingEnable=hpnicfFCoEFIPSnoopingEnable, hpnicfFCoECfgDATov=hpnicfFCoECfgDATov, hpnicfFCoEStaticVfcCreationTime=hpnicfFCoEStaticVfcCreationTime, hpnicfFCoEStaticVfcFCFPriority=hpnicfFCoEStaticVfcFCFPriority, hpnicfFCoEVLANEntry=hpnicfFCoEVLANEntry, hpnicfFCoEConfig=hpnicfFCoEConfig, hpnicfFCoEObjects=hpnicfFCoEObjects, hpnicfFCoECfgDynamicVfcCreation=hpnicfFCoECfgDynamicVfcCreation, hpnicfFCoEStaticVfcIfIndex=hpnicfFCoEStaticVfcIfIndex, hpnicfFCoEStaticVfcEntry=hpnicfFCoEStaticVfcEntry, hpnicfFCoEStaticVfcFailureCause=hpnicfFCoEStaticVfcFailureCause, hpnicfFCoEFIPSnoopingTable=hpnicfFCoEFIPSnoopingTable, hpnicfFCoEStaticVfcBindMACAddress=hpnicfFCoEStaticVfcBindMACAddress, hpnicfFCoEStaticVfcTable=hpnicfFCoEStaticVfcTable, hpnicfFCoECfgTable=hpnicfFCoECfgTable, hpnicfFCoEStaticVfcBindType=hpnicfFCoEStaticVfcBindType, hpnicfFCoEFabricIndex=hpnicfFCoEFabricIndex, hpnicfFCoE=hpnicfFCoE, hpnicfFCoEFIPSnoopingFcmap=hpnicfFCoEFIPSnoopingFcmap, hpnicfFCoEVLANRowStatus=hpnicfFCoEVLANRowStatus, hpnicfFCoEVLANTable=hpnicfFCoEVLANTable, hpnicfFCoEVLANIndex=hpnicfFCoEVLANIndex)
