#
# PySNMP MIB module PDN-MPE-HEALTH-AND-STATUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-MPE-HEALTH-AND-STATUS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:39:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
mpe_devHealth, = mibBuilder.importSymbols("PDN-HEADER-MIB", "mpe-devHealth")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Bits, NotificationType, MibIdentifier, NotificationType, Integer32, ObjectIdentity, Counter64, iso, IpAddress, ModuleIdentity, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Bits", "NotificationType", "MibIdentifier", "NotificationType", "Integer32", "ObjectIdentity", "Counter64", "iso", "IpAddress", "ModuleIdentity", "Counter32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mpeDevHealthAndStatusMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 7, 1))
mpeDevHealthAndStatusMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 7, 2))
mpeDevHealthAndStatusTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 7, 1, 1), )
if mibBuilder.loadTexts: mpeDevHealthAndStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: mpeDevHealthAndStatusTable.setDescription("A table that contains information about an Entity's health.")
mpeDevHealthAndStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 7, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: mpeDevHealthAndStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mpeDevHealthAndStatusEntry.setDescription("A list of information for an entity's health.")
mpeDevSelfTestResults = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 7, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpeDevSelfTestResults.setStatus('mandatory')
if mibBuilder.loadTexts: mpeDevSelfTestResults.setDescription('Self-test results. Self-test (or power-up test) results summarizes the test results of each CCA, where each CCA test result is separated by a semi-colon. Refer to device-specific user documentation for a complete description of the self test codes and messages.')
mpeSelfTestFailure = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 7, 2) + (0,1)).setObjects(("PDN-MPE-HEALTH-AND-STATUS-MIB", "mpeDevSelfTestResults"))
if mibBuilder.loadTexts: mpeSelfTestFailure.setDescription("This trap signifies that the sending protocol's device has failed self test. The variable binding for this trap would be the selfTest devSelfTestResults object of the Health and Status MIB. The exact format of this display string will be well-documented in the Operational Specifications of the device.")
mibBuilder.exportSymbols("PDN-MPE-HEALTH-AND-STATUS-MIB", mpeDevHealthAndStatusEntry=mpeDevHealthAndStatusEntry, mpeDevHealthAndStatusTable=mpeDevHealthAndStatusTable, mpeDevHealthAndStatusMIBTraps=mpeDevHealthAndStatusMIBTraps, mpeDevHealthAndStatusMIBObjects=mpeDevHealthAndStatusMIBObjects, mpeDevSelfTestResults=mpeDevSelfTestResults, mpeSelfTestFailure=mpeSelfTestFailure)
