#
# PySNMP MIB module MEMOTEC-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MEMOTEC-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 18:11:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, iso, Bits, TimeTicks, Counter32, Counter64, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, enterprises, NotificationType, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "Bits", "TimeTicks", "Counter32", "Counter64", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "enterprises", "NotificationType", "ModuleIdentity", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
memotec = MibIdentifier((1, 3, 6, 1, 4, 1, 495))
memotecExperimental = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 1))
memotecProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2))
memotecAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 3))
ems221Trap = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 4))
cxProduct = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1))
mibBuilder.exportSymbols("MEMOTEC-SMI", cxProduct=cxProduct, memotecProducts=memotecProducts, memotecExperimental=memotecExperimental, memotecAdmin=memotecAdmin, memotec=memotec, ems221Trap=ems221Trap)
