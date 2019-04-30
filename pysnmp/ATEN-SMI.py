#
# PySNMP MIB module ATEN-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ATEN-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 17:14:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, MibIdentifier, ObjectIdentity, Counter64, Gauge32, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Counter32, iso, NotificationType, Unsigned32, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "ObjectIdentity", "Counter64", "Gauge32", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Counter32", "iso", "NotificationType", "Unsigned32", "Integer32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aten = MibIdentifier((1, 3, 6, 1, 4, 1, 21317))
atenProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 21317, 1))
otherEnterprises = MibIdentifier((1, 3, 6, 1, 4, 1, 21317, 2))
atenExperiment = MibIdentifier((1, 3, 6, 1, 4, 1, 21317, 3))
mibBuilder.exportSymbols("ATEN-SMI", otherEnterprises=otherEnterprises, aten=aten, atenProducts=atenProducts, atenExperiment=atenExperiment)
