#
# PySNMP MIB module JohnsonControlsInc-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JohnsonControlsInc-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:47:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Unsigned32, Counter64, MibIdentifier, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "Counter64", "MibIdentifier", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
private = MibIdentifier((1, 3, 6, 1, 4))
enterprises = MibIdentifier((1, 3, 6, 1, 4, 1))
johnsonControlsInc = MibIdentifier((1, 3, 6, 1, 4, 1, 4399))
corporate = MibIdentifier((1, 3, 6, 1, 4, 1, 4399, 1))
jciControlsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4399, 2))
mibBuilder.exportSymbols("JohnsonControlsInc-MIB", jciControlsGroup=jciControlsGroup, johnsonControlsInc=johnsonControlsInc, enterprises=enterprises, corporate=corporate, private=private)
