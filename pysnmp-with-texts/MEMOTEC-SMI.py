#
# PySNMP MIB module MEMOTEC-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MEMOTEC-SMI
# Produced by pysmi-0.3.4 at Wed May  1 12:26:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, Gauge32, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, MibIdentifier, NotificationType, Unsigned32, ObjectIdentity, Bits, iso, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Gauge32", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "MibIdentifier", "NotificationType", "Unsigned32", "ObjectIdentity", "Bits", "iso", "TimeTicks", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
memotec = MibIdentifier((1, 3, 6, 1, 4, 1, 495))
memotecExperimental = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 1))
memotecProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2))
memotecAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 3))
ems221Trap = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 4))
cxProduct = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1))
mibBuilder.exportSymbols("MEMOTEC-SMI", memotecAdmin=memotecAdmin, memotecProducts=memotecProducts, memotec=memotec, cxProduct=cxProduct, ems221Trap=ems221Trap, memotecExperimental=memotecExperimental)
