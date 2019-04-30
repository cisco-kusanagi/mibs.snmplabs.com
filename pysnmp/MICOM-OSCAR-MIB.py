#
# PySNMP MIB module MICOM-OSCAR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MICOM-OSCAR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:01:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, Counter32, Counter64, Integer32, Gauge32, IpAddress, ModuleIdentity, MibIdentifier, Bits, TimeTicks, enterprises, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "Counter32", "Counter64", "Integer32", "Gauge32", "IpAddress", "ModuleIdentity", "MibIdentifier", "Bits", "TimeTicks", "enterprises", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
micom = MibIdentifier((1, 3, 6, 1, 4, 1, 335))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1))
micom_oscar = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4)).setLabel("micom-oscar")
mibBuilder.exportSymbols("MICOM-OSCAR-MIB", products=products, micom_oscar=micom_oscar, micom=micom)
