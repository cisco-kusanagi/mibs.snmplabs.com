#
# PySNMP MIB module ACCORD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ACCORD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:57:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Bits, Gauge32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, enterprises, IpAddress, ModuleIdentity, Unsigned32, iso, ObjectIdentity, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "Gauge32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "enterprises", "IpAddress", "ModuleIdentity", "Unsigned32", "iso", "ObjectIdentity", "MibIdentifier", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
accord = MibIdentifier((1, 3, 6, 1, 4, 1, 6333))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 6333, 1))
mgc_100 = MibIdentifier((1, 3, 6, 1, 4, 1, 6333, 1, 1)).setLabel("mgc-100")
mibBuilder.exportSymbols("ACCORD-MIB", accord=accord, mgc_100=mgc_100, products=products)
