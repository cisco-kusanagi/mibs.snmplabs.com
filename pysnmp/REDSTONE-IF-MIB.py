#
# PySNMP MIB module REDSTONE-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/REDSTONE-IF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:46:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ifStackHigherLayer, ifStackLowerLayer, ifEntry = mibBuilder.importSymbols("IF-MIB", "ifStackHigherLayer", "ifStackLowerLayer", "ifEntry")
rsMgmt, = mibBuilder.importSymbols("REDSTONE-SMI", "rsMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Unsigned32, Gauge32, ModuleIdentity, Counter32, Integer32, MibIdentifier, ObjectIdentity, IpAddress, NotificationType, Counter64, TimeTicks, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Gauge32", "ModuleIdentity", "Counter32", "Integer32", "MibIdentifier", "ObjectIdentity", "IpAddress", "NotificationType", "Counter64", "TimeTicks", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
rsIfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2773, 2, 3))
rsIfMIB.setRevisions(('1998-01-01 00:00',))
if mibBuilder.loadTexts: rsIfMIB.setLastUpdated('9801010000Z')
if mibBuilder.loadTexts: rsIfMIB.setOrganization('Redstone Communications, Inc.')
rsInterfaces = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 3, 1))
rsIf = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1))
class RsIfType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("ip", 0), ("ppp", 1), ("ds0", 2), ("ds1", 3), ("ds3", 4), ("frameRelay", 5), ("ethernet", 6), ("sonet", 7), ("sonetPath", 8), ("atm", 9), ("aal5", 10), ("atmSubInterface", 11), ("ft1", 12), ("hdlc", 13), ("ipLoopback", 14), ("ipVirtual", 15), ("frSubInterface", 16), ("pppoe", 17), ("pppoeSubInterface", 18))

rsIfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 1))
rsIfTable = MibTable((1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 1, 1), )
if mibBuilder.loadTexts: rsIfTable.setStatus('current')
rsIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 1, 1, 1), )
ifEntry.registerAugmentions(("REDSTONE-IF-MIB", "rsIfEntry"))
rsIfEntry.setIndexNames(*ifEntry.getIndexNames())
if mibBuilder.loadTexts: rsIfEntry.setStatus('current')
rsIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 1, 1, 1, 1), RsIfType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfType.setStatus('current')
rsIfInvStackTable = MibTable((1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 1, 2), )
if mibBuilder.loadTexts: rsIfInvStackTable.setStatus('current')
rsIfInvStackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifStackLowerLayer"), (0, "IF-MIB", "ifStackHigherLayer"))
if mibBuilder.loadTexts: rsIfInvStackEntry.setStatus('current')
rsIfInvStackStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 1, 2, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfInvStackStatus.setStatus('current')
rsIfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 4))
rsIfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 4, 1))
rsIfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 4, 2))
rsIfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 4, 1, 1)).setObjects(("REDSTONE-IF-MIB", "rsIfGroup"), ("REDSTONE-IF-MIB", "rsIfInvStackGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsIfCompliance = rsIfCompliance.setStatus('current')
rsIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 4, 2, 1)).setObjects(("REDSTONE-IF-MIB", "rsIfType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsIfGroup = rsIfGroup.setStatus('current')
rsIfInvStackGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 4, 2, 2)).setObjects(("REDSTONE-IF-MIB", "rsIfInvStackStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsIfInvStackGroup = rsIfInvStackGroup.setStatus('current')
mibBuilder.exportSymbols("REDSTONE-IF-MIB", rsIfInvStackTable=rsIfInvStackTable, rsIfConformance=rsIfConformance, rsIfCompliance=rsIfCompliance, rsIfCompliances=rsIfCompliances, rsIfEntry=rsIfEntry, rsIfGroup=rsIfGroup, rsIfMIB=rsIfMIB, rsIf=rsIf, rsIfInvStackGroup=rsIfInvStackGroup, rsIfType=rsIfType, PYSNMP_MODULE_ID=rsIfMIB, rsInterfaces=rsInterfaces, rsIfInvStackStatus=rsIfInvStackStatus, rsIfGroups=rsIfGroups, rsIfObjects=rsIfObjects, RsIfType=RsIfType, rsIfInvStackEntry=rsIfInvStackEntry, rsIfTable=rsIfTable)
