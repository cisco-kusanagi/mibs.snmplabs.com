#
# PySNMP MIB module A3COM-HUAWEI-L2ISOLATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-L2ISOLATE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:05:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Unsigned32, Integer32, Counter64, Gauge32, IpAddress, MibIdentifier, iso, ModuleIdentity, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "Integer32", "Counter64", "Gauge32", "IpAddress", "MibIdentifier", "iso", "ModuleIdentity", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType")
MacAddress, TruthValue, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TruthValue", "RowStatus", "DisplayString", "TextualConvention")
h3cL2Isolate = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 103))
h3cL2Isolate.setRevisions(('2009-05-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h3cL2Isolate.setRevisionsDescriptions(('Initial version',))
if mibBuilder.loadTexts: h3cL2Isolate.setLastUpdated('200905060000Z')
if mibBuilder.loadTexts: h3cL2Isolate.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cL2Isolate.setContactInfo('Platform Team H3C Technologies Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip: 100085')
if mibBuilder.loadTexts: h3cL2Isolate.setDescription('The MIB module is used for l2 isolation.')
h3cL2IsolateObject = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 103, 1))
h3cL2IsolateEnableTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 103, 1, 1), )
if mibBuilder.loadTexts: h3cL2IsolateEnableTable.setStatus('current')
if mibBuilder.loadTexts: h3cL2IsolateEnableTable.setDescription('A table for enabling/disabling layer-2-isolate for VLAN.')
h3cL2IsolateEnableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 103, 1, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-L2ISOLATE-MIB", "h3cL2IsolateVLANIndex"))
if mibBuilder.loadTexts: h3cL2IsolateEnableEntry.setStatus('current')
if mibBuilder.loadTexts: h3cL2IsolateEnableEntry.setDescription('An entry for enabling/disabling layer-2-isolate for VLAN.')
h3cL2IsolateVLANIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 103, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: h3cL2IsolateVLANIndex.setStatus('current')
if mibBuilder.loadTexts: h3cL2IsolateVLANIndex.setDescription('Represents index of VLAN for layer-2-isolate.')
h3cL2IsolateEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 103, 1, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cL2IsolateEnable.setStatus('current')
if mibBuilder.loadTexts: h3cL2IsolateEnable.setDescription('Represents the layer-2-isolate status of VLAN.')
h3cL2IsolatePermitMACTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 103, 1, 2), )
if mibBuilder.loadTexts: h3cL2IsolatePermitMACTable.setStatus('current')
if mibBuilder.loadTexts: h3cL2IsolatePermitMACTable.setDescription('A table represents the permitting MAC address for the specific VLAN.')
h3cL2IsolatePermitMACEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 103, 1, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-L2ISOLATE-MIB", "h3cL2IsolateVLANIndex"), (0, "A3COM-HUAWEI-L2ISOLATE-MIB", "h3cL2IsoLatePermitMAC"))
if mibBuilder.loadTexts: h3cL2IsolatePermitMACEntry.setStatus('current')
if mibBuilder.loadTexts: h3cL2IsolatePermitMACEntry.setDescription('Each entry represents the permitting MAC address for the specific VLAN.')
h3cL2IsoLatePermitMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 103, 1, 2, 1, 1), MacAddress())
if mibBuilder.loadTexts: h3cL2IsoLatePermitMAC.setStatus('current')
if mibBuilder.loadTexts: h3cL2IsoLatePermitMAC.setDescription('Represents the MAC address permitted in the VLAN.')
h3cL2IsoLatePermitMACRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 103, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cL2IsoLatePermitMACRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cL2IsoLatePermitMACRowStatus.setDescription('RowStatus. Three actions are used: active, CreateAndGo, destroy.')
mibBuilder.exportSymbols("A3COM-HUAWEI-L2ISOLATE-MIB", h3cL2Isolate=h3cL2Isolate, h3cL2IsolatePermitMACTable=h3cL2IsolatePermitMACTable, h3cL2IsolatePermitMACEntry=h3cL2IsolatePermitMACEntry, h3cL2IsolateEnableTable=h3cL2IsolateEnableTable, h3cL2IsolateObject=h3cL2IsolateObject, h3cL2IsoLatePermitMACRowStatus=h3cL2IsoLatePermitMACRowStatus, h3cL2IsoLatePermitMAC=h3cL2IsoLatePermitMAC, h3cL2IsolateEnableEntry=h3cL2IsolateEnableEntry, PYSNMP_MODULE_ID=h3cL2Isolate, h3cL2IsolateEnable=h3cL2IsolateEnable, h3cL2IsolateVLANIndex=h3cL2IsolateVLANIndex)
