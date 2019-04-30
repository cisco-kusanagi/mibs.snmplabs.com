#
# PySNMP MIB module ZYXEL-OAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-OAM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:45:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, NotificationType, Counter64, TimeTicks, iso, Counter32, Gauge32, ObjectIdentity, IpAddress, MibIdentifier, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Counter64", "TimeTicks", "iso", "Counter32", "Gauge32", "ObjectIdentity", "IpAddress", "MibIdentifier", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelOam = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56))
if mibBuilder.loadTexts: zyxelOam.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelOam.setOrganization('Enterprise Solution ZyXEL')
zyxelOamSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 1))
zyOamState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyOamState.setStatus('current')
zyxelOamPortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 1, 2), )
if mibBuilder.loadTexts: zyxelOamPortTable.setStatus('current')
zyxelOamPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: zyxelOamPortEntry.setStatus('current')
zyOamPortFunctionsSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 1, 2, 1, 1), Bits().clone(namedValues=NamedValues(("unidirectionalSupport", 0), ("loopbackSupport", 1), ("eventSupport", 2), ("variableSupport", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyOamPortFunctionsSupported.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-OAM-MIB", zyxelOam=zyxelOam, zyOamState=zyOamState, PYSNMP_MODULE_ID=zyxelOam, zyxelOamPortEntry=zyxelOamPortEntry, zyxelOamSetup=zyxelOamSetup, zyxelOamPortTable=zyxelOamPortTable, zyOamPortFunctionsSupported=zyOamPortFunctionsSupported)
