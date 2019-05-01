#
# PySNMP MIB module ATEN-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ATEN-SMI
# Produced by pysmi-0.3.4 at Wed May  1 11:30:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, ModuleIdentity, iso, Integer32, enterprises, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, ObjectIdentity, NotificationType, TimeTicks, Counter32, Unsigned32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "iso", "Integer32", "enterprises", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "ObjectIdentity", "NotificationType", "TimeTicks", "Counter32", "Unsigned32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
aten = MibIdentifier((1, 3, 6, 1, 4, 1, 21317))
atenProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 21317, 1))
otherEnterprises = MibIdentifier((1, 3, 6, 1, 4, 1, 21317, 2))
atenExperiment = MibIdentifier((1, 3, 6, 1, 4, 1, 21317, 3))
mibBuilder.exportSymbols("ATEN-SMI", atenExperiment=atenExperiment, atenProducts=atenProducts, aten=aten, otherEnterprises=otherEnterprises)
