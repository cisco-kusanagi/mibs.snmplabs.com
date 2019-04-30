#
# PySNMP MIB module VERAX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VERAX-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:26:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleIdentity, = mibBuilder.importSymbols("RFC1155-SMI", "ModuleIdentity")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, ObjectIdentity, Counter64, Gauge32, enterprises, ModuleIdentity, Bits, IpAddress, NotificationType, Counter32, iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "Counter64", "Gauge32", "enterprises", "ModuleIdentity", "Bits", "IpAddress", "NotificationType", "Counter32", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
veraxMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21340))
if mibBuilder.loadTexts: veraxMIB.setLastUpdated('201211051200Z')
if mibBuilder.loadTexts: veraxMIB.setOrganization('Verax Systems')
products = MibIdentifier((1, 3, 6, 1, 4, 1, 21340, 1))
veraxnms = MibIdentifier((1, 3, 6, 1, 4, 1, 21340, 1, 2))
mibBuilder.exportSymbols("VERAX-MIB", products=products, PYSNMP_MODULE_ID=veraxMIB, veraxnms=veraxnms, veraxMIB=veraxMIB)
