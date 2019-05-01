#
# PySNMP MIB module MICOM-OSCAR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MICOM-OSCAR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:12:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, TimeTicks, Counter64, Bits, Gauge32, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "TimeTicks", "Counter64", "Bits", "Gauge32", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "iso", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
micom = MibIdentifier((1, 3, 6, 1, 4, 1, 335))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1))
micom_oscar = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4)).setLabel("micom-oscar")
mibBuilder.exportSymbols("MICOM-OSCAR-MIB", micom_oscar=micom_oscar, products=products, micom=micom)
