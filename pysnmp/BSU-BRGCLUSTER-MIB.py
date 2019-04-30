#
# PySNMP MIB module BSU-BRGCLUSTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BSU-BRGCLUSTER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:24:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
bsu, = mibBuilder.importSymbols("ANIROOT-MIB", "bsu")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType, IpAddress, TimeTicks, Bits, Counter64, Gauge32, iso, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType", "IpAddress", "TimeTicks", "Bits", "Counter64", "Gauge32", "iso", "Integer32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
aniBsuBridge = ModuleIdentity((1, 3, 6, 1, 4, 1, 4325, 3, 5))
if mibBuilder.loadTexts: aniBsuBridge.setLastUpdated('0209251530Z')
if mibBuilder.loadTexts: aniBsuBridge.setOrganization('Aperto Networks')
aniBsuSuBridgeEnable = MibScalar((1, 3, 6, 1, 4, 1, 4325, 3, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("not-applicable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniBsuSuBridgeEnable.setStatus('current')
mibBuilder.exportSymbols("BSU-BRGCLUSTER-MIB", aniBsuSuBridgeEnable=aniBsuSuBridgeEnable, aniBsuBridge=aniBsuBridge, PYSNMP_MODULE_ID=aniBsuBridge)
