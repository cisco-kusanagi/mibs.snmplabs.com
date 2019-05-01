#
# PySNMP MIB module EXTREMEdot11f-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:07:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
extremeAP, = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAP")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, IpAddress, Integer32, Gauge32, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, ModuleIdentity, ObjectIdentity, TimeTicks, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "Integer32", "Gauge32", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "Bits", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
extremeDot11f = ModuleIdentity((1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 22))
if mibBuilder.loadTexts: extremeDot11f.setLastUpdated('0107020000Z')
if mibBuilder.loadTexts: extremeDot11f.setOrganization('Extreme Networks')
if mibBuilder.loadTexts: extremeDot11f.setContactInfo(' ')
if mibBuilder.loadTexts: extremeDot11f.setDescription('This MIB module provides management of IAPP on a set of APs. It is functionally identical to the IAPP MIB from the IEEE with the addition of a new index.')
mibBuilder.exportSymbols("EXTREMEdot11f-MIB", extremeDot11f=extremeDot11f, PYSNMP_MODULE_ID=extremeDot11f)
