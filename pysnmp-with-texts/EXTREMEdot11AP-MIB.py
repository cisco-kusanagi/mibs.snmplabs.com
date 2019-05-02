#
# PySNMP MIB module EXTREMEdot11AP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:07:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
extremeAP, = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAP")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, IpAddress, Integer32, Gauge32, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, ModuleIdentity, ObjectIdentity, TimeTicks, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "Integer32", "Gauge32", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "Bits", "Unsigned32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
extremeDot11ap = ModuleIdentity((1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 21))
if mibBuilder.loadTexts: extremeDot11ap.setLastUpdated('0211140000Z')
if mibBuilder.loadTexts: extremeDot11ap.setOrganization('Extreme Networks')
if mibBuilder.loadTexts: extremeDot11ap.setContactInfo(' ')
if mibBuilder.loadTexts: extremeDot11ap.setDescription('This MIB module provides managemetn of a set of APs. It is based on the IEEE AP MIB with additions for better indexing.')
mibBuilder.exportSymbols("EXTREMEdot11AP-MIB", extremeDot11ap=extremeDot11ap, PYSNMP_MODULE_ID=extremeDot11ap)
