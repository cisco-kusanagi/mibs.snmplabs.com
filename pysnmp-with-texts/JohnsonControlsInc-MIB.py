#
# PySNMP MIB module JohnsonControlsInc-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JohnsonControlsInc-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:58:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, Bits, ModuleIdentity, ObjectIdentity, Unsigned32, Integer32, TimeTicks, IpAddress, Counter32, iso, Gauge32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "Bits", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "Integer32", "TimeTicks", "IpAddress", "Counter32", "iso", "Gauge32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
private = MibIdentifier((1, 3, 6, 1, 4))
enterprises = MibIdentifier((1, 3, 6, 1, 4, 1))
johnsonControlsInc = MibIdentifier((1, 3, 6, 1, 4, 1, 4399))
corporate = MibIdentifier((1, 3, 6, 1, 4, 1, 4399, 1))
jciControlsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4399, 2))
mibBuilder.exportSymbols("JohnsonControlsInc-MIB", private=private, jciControlsGroup=jciControlsGroup, johnsonControlsInc=johnsonControlsInc, enterprises=enterprises, corporate=corporate)
