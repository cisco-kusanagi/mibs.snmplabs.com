#
# PySNMP MIB module H3C-VOICE-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-VOICE-VLAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:11:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Bits, NotificationType, Unsigned32, IpAddress, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, Gauge32, iso, ObjectIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "NotificationType", "Unsigned32", "IpAddress", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "Gauge32", "iso", "ObjectIdentity", "Counter32")
RowStatus, DisplayString, MacAddress, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "MacAddress", "TextualConvention", "TruthValue")
h3cVoiceVlan = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 9))
h3cVoiceVlan.setRevisions(('2009-05-15 00:00', '2002-07-01 00:00',))
if mibBuilder.loadTexts: h3cVoiceVlan.setLastUpdated('200905150000Z')
if mibBuilder.loadTexts: h3cVoiceVlan.setOrganization('H3C Tech, Inc.')
class PortList(TextualConvention, OctetString):
    status = 'current'

h3cvoiceVlanOuiTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 9, 1), )
if mibBuilder.loadTexts: h3cvoiceVlanOuiTable.setStatus('current')
h3cvoiceVlanOuiEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 9, 1, 1), ).setIndexNames((0, "H3C-VOICE-VLAN-MIB", "h3cVoiceVlanOuiAddress"))
if mibBuilder.loadTexts: h3cvoiceVlanOuiEntry.setStatus('current')
h3cVoiceVlanOuiAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 9, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoiceVlanOuiAddress.setStatus('current')
h3cVoiceVlanOuiMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 9, 1, 1, 2), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoiceVlanOuiMask.setStatus('current')
h3cVoiceVlanOuiDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 9, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoiceVlanOuiDescription.setStatus('current')
h3cVoiceVlanOuiRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 9, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoiceVlanOuiRowStatus.setStatus('current')
h3cVoiceVlanEnabledId = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 9, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoiceVlanEnabledId.setStatus('current')
h3cVoiceVlanPortEnableList = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 9, 3), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoiceVlanPortEnableList.setStatus('current')
h3cVoiceVlanAgingTime = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 9, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 43200)).clone(1440)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoiceVlanAgingTime.setStatus('current')
h3cVoiceVlanConfigState = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 9, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("auto", 1), ("manual", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoiceVlanConfigState.setStatus('current')
h3cVoiceVlanSecurityState = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 9, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("security", 1), ("normal", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoiceVlanSecurityState.setStatus('current')
h3cvoiceVlanPortTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 9, 7), )
if mibBuilder.loadTexts: h3cvoiceVlanPortTable.setStatus('current')
h3cvoiceVlanPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 9, 7, 1), ).setIndexNames((0, "H3C-VOICE-VLAN-MIB", "h3cVoiceVlanPortifIndex"))
if mibBuilder.loadTexts: h3cvoiceVlanPortEntry.setStatus('current')
h3cVoiceVlanPortifIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 9, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cVoiceVlanPortifIndex.setStatus('current')
h3cVoiceVlanPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 9, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("auto", 1), ("manual", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoiceVlanPortMode.setStatus('current')
h3cVoiceVlanPortLegacy = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 9, 7, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoiceVlanPortLegacy.setStatus('current')
h3cVoiceVlanPortQosTrust = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 9, 7, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoiceVlanPortQosTrust.setStatus('current')
mibBuilder.exportSymbols("H3C-VOICE-VLAN-MIB", PortList=PortList, h3cVoiceVlanPortEnableList=h3cVoiceVlanPortEnableList, h3cvoiceVlanOuiEntry=h3cvoiceVlanOuiEntry, h3cVoiceVlanPortQosTrust=h3cVoiceVlanPortQosTrust, h3cVoiceVlanOuiRowStatus=h3cVoiceVlanOuiRowStatus, h3cVoiceVlan=h3cVoiceVlan, h3cVoiceVlanOuiMask=h3cVoiceVlanOuiMask, h3cvoiceVlanPortTable=h3cvoiceVlanPortTable, h3cVoiceVlanSecurityState=h3cVoiceVlanSecurityState, h3cvoiceVlanOuiTable=h3cvoiceVlanOuiTable, PYSNMP_MODULE_ID=h3cVoiceVlan, h3cVoiceVlanAgingTime=h3cVoiceVlanAgingTime, h3cVoiceVlanConfigState=h3cVoiceVlanConfigState, h3cVoiceVlanOuiDescription=h3cVoiceVlanOuiDescription, h3cVoiceVlanEnabledId=h3cVoiceVlanEnabledId, h3cVoiceVlanPortLegacy=h3cVoiceVlanPortLegacy, h3cvoiceVlanPortEntry=h3cvoiceVlanPortEntry, h3cVoiceVlanPortMode=h3cVoiceVlanPortMode, h3cVoiceVlanOuiAddress=h3cVoiceVlanOuiAddress, h3cVoiceVlanPortifIndex=h3cVoiceVlanPortifIndex)
