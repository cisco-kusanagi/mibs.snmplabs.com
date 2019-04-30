#
# PySNMP MIB module SanAppliance-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SanAppliance-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:07:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Gauge32, ObjectIdentity, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, IpAddress, MibIdentifier, Integer32, NotificationType, Unsigned32, Counter64, Counter32, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "ObjectIdentity", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "IpAddress", "MibIdentifier", "Integer32", "NotificationType", "Unsigned32", "Counter64", "Counter32", "NotificationType", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dell = MibIdentifier((1, 3, 6, 1, 4, 1, 674))
storage = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10893))
sanRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10893, 2))
sanAppliance = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10893, 2, 1))
sanApplGlobalStatus = MibScalar((1, 3, 6, 1, 4, 1, 674, 10893, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("critical", 1), ("warning", 2), ("normal", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sanApplGlobalStatus.setStatus('mandatory')
sanApplEvts = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10893, 2, 1, 200))
sanApplName = MibScalar((1, 3, 6, 1, 4, 1, 674, 10893, 2, 1, 200, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sanApplName.setStatus('mandatory')
sanApplFailed = NotificationType((1, 3, 6, 1, 4, 1, 674, 10893, 2, 1, 200) + (0,1)).setObjects(("SanAppliance-MIB", "sanApplName"))
sanApplNormal = NotificationType((1, 3, 6, 1, 4, 1, 674, 10893, 2, 1, 200) + (0,2)).setObjects(("SanAppliance-MIB", "sanApplName"))
sanApplStarted = NotificationType((1, 3, 6, 1, 4, 1, 674, 10893, 2, 1, 200) + (0,3)).setObjects(("SanAppliance-MIB", "sanApplName"))
sanApplStopped = NotificationType((1, 3, 6, 1, 4, 1, 674, 10893, 2, 1, 200) + (0,4)).setObjects(("SanAppliance-MIB", "sanApplName"))
mibBuilder.exportSymbols("SanAppliance-MIB", sanRoot=sanRoot, sanApplStopped=sanApplStopped, sanApplName=sanApplName, dell=dell, sanApplNormal=sanApplNormal, sanAppliance=sanAppliance, sanApplStarted=sanApplStarted, sanApplGlobalStatus=sanApplGlobalStatus, sanApplFailed=sanApplFailed, storage=storage, sanApplEvts=sanApplEvts)
