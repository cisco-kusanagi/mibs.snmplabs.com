#
# PySNMP MIB module GBNL2PppoePlus-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GBNL2PppoePlus-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:04:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
gbnL2, = mibBuilder.importSymbols("GREENTECH-MASTER-MIB", "gbnL2")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, MibIdentifier, Unsigned32, Bits, iso, Counter64, NotificationType, Counter32, ObjectIdentity, TimeTicks, ModuleIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "Unsigned32", "Bits", "iso", "Counter64", "NotificationType", "Counter32", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
RowStatus, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "TextualConvention", "DisplayString")
gbnL2PppoePlus = ModuleIdentity((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 6))
gbnL2PppoePlus.setRevisions(('1907-11-22 00:00',))
if mibBuilder.loadTexts: gbnL2PppoePlus.setLastUpdated('0711220000Z')
if mibBuilder.loadTexts: gbnL2PppoePlus.setOrganization('Greentech')
pppoeplusOnOff = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 6, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppoeplusOnOff.setStatus('current')
pppoeplusType = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 6, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("standard", 0), ("huawei", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppoeplusType.setStatus('current')
mibBuilder.exportSymbols("GBNL2PppoePlus-MIB", pppoeplusOnOff=pppoeplusOnOff, pppoeplusType=pppoeplusType, PYSNMP_MODULE_ID=gbnL2PppoePlus, gbnL2PppoePlus=gbnL2PppoePlus)
