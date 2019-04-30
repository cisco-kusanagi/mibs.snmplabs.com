#
# PySNMP MIB module Q-IN-Q-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Q-IN-Q-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:34:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, NotificationType, ObjectIdentity, ModuleIdentity, Counter32, IpAddress, Bits, Gauge32, MibIdentifier, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "ObjectIdentity", "ModuleIdentity", "Counter32", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso")
TextualConvention, DisplayString, MacAddress, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "MacAddress", "RowStatus")
swQinQMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 57))
if mibBuilder.loadTexts: swQinQMIB.setLastUpdated('0804080000Z')
if mibBuilder.loadTexts: swQinQMIB.setOrganization('D-Link Corp.')
class VlanId(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

swQinQCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 57, 1))
swQinQInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 57, 2))
swQinQPortMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 57, 3))
swQinQMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 57, 4))
swQinQState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 57, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swQinQState.setStatus('current')
swQinQPortTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 1), )
if mibBuilder.loadTexts: swQinQPortTable.setStatus('current')
swQinQPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 1, 1), ).setIndexNames((0, "Q-IN-Q-MIB", "swQinQPortIndex"))
if mibBuilder.loadTexts: swQinQPortEntry.setStatus('current')
swQinQPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swQinQPortIndex.setStatus('current')
swQinQPortRole = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("nni", 1), ("uni", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swQinQPortRole.setStatus('current')
swQinQPortTpid = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swQinQPortTpid.setStatus('current')
mibBuilder.exportSymbols("Q-IN-Q-MIB", swQinQPortTpid=swQinQPortTpid, swQinQMIB=swQinQMIB, swQinQState=swQinQState, swQinQMgmt=swQinQMgmt, swQinQCtrl=swQinQCtrl, PYSNMP_MODULE_ID=swQinQMIB, swQinQPortTable=swQinQPortTable, swQinQInfo=swQinQInfo, swQinQPortEntry=swQinQPortEntry, swQinQPortRole=swQinQPortRole, VlanId=VlanId, swQinQPortMgmt=swQinQPortMgmt, swQinQPortIndex=swQinQPortIndex)
