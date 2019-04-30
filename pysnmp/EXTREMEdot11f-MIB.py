#
# PySNMP MIB module EXTREMEdot11f-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:53:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
extremeAP, = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAP")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, MibIdentifier, ModuleIdentity, Counter64, Counter32, NotificationType, Integer32, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "MibIdentifier", "ModuleIdentity", "Counter64", "Counter32", "NotificationType", "Integer32", "IpAddress", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
extremeDot11f = ModuleIdentity((1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 22))
if mibBuilder.loadTexts: extremeDot11f.setLastUpdated('0107020000Z')
if mibBuilder.loadTexts: extremeDot11f.setOrganization('Extreme Networks')
mibBuilder.exportSymbols("EXTREMEdot11f-MIB", PYSNMP_MODULE_ID=extremeDot11f, extremeDot11f=extremeDot11f)
