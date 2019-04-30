#
# PySNMP MIB module PDN-MPE-HEALTH-AND-STATUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-MPE-HEALTH-AND-STATUS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:30:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
mpe_devHealth, = mibBuilder.importSymbols("PDN-HEADER-MIB", "mpe-devHealth")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, NotificationType, ModuleIdentity, Unsigned32, iso, NotificationType, IpAddress, Counter32, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "NotificationType", "ModuleIdentity", "Unsigned32", "iso", "NotificationType", "IpAddress", "Counter32", "Integer32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mpeDevHealthAndStatusMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 7, 1))
mpeDevHealthAndStatusMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 7, 2))
mpeDevHealthAndStatusTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 7, 1, 1), )
if mibBuilder.loadTexts: mpeDevHealthAndStatusTable.setStatus('mandatory')
mpeDevHealthAndStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 7, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: mpeDevHealthAndStatusEntry.setStatus('mandatory')
mpeDevSelfTestResults = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 7, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpeDevSelfTestResults.setStatus('mandatory')
mpeSelfTestFailure = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 7, 2) + (0,1)).setObjects(("PDN-MPE-HEALTH-AND-STATUS-MIB", "mpeDevSelfTestResults"))
mibBuilder.exportSymbols("PDN-MPE-HEALTH-AND-STATUS-MIB", mpeDevHealthAndStatusMIBTraps=mpeDevHealthAndStatusMIBTraps, mpeDevHealthAndStatusTable=mpeDevHealthAndStatusTable, mpeDevSelfTestResults=mpeDevSelfTestResults, mpeDevHealthAndStatusEntry=mpeDevHealthAndStatusEntry, mpeDevHealthAndStatusMIBObjects=mpeDevHealthAndStatusMIBObjects, mpeSelfTestFailure=mpeSelfTestFailure)
