#
# PySNMP MIB module ACCORD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ACCORD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:12:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, Integer32, ModuleIdentity, Gauge32, enterprises, iso, Counter64, NotificationType, Bits, MibIdentifier, IpAddress, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "Integer32", "ModuleIdentity", "Gauge32", "enterprises", "iso", "Counter64", "NotificationType", "Bits", "MibIdentifier", "IpAddress", "Counter32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
accord = MibIdentifier((1, 3, 6, 1, 4, 1, 6333))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 6333, 1))
mgc_100 = MibIdentifier((1, 3, 6, 1, 4, 1, 6333, 1, 1)).setLabel("mgc-100")
mibBuilder.exportSymbols("ACCORD-MIB", accord=accord, mgc_100=mgc_100, products=products)
