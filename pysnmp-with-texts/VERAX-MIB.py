#
# PySNMP MIB module VERAX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VERAX-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:33:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleIdentity, = mibBuilder.importSymbols("RFC1155-SMI", "ModuleIdentity")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Bits, enterprises, Counter32, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, Counter64, ModuleIdentity, Integer32, iso, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Bits", "enterprises", "Counter32", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "Counter64", "ModuleIdentity", "Integer32", "iso", "TimeTicks", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
veraxMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21340))
if mibBuilder.loadTexts: veraxMIB.setLastUpdated('201211051200Z')
if mibBuilder.loadTexts: veraxMIB.setOrganization('Verax Systems')
if mibBuilder.loadTexts: veraxMIB.setContactInfo('Verax Systems Corp. E-mail: office@veraxsystems.com')
if mibBuilder.loadTexts: veraxMIB.setDescription('This MIB is the base Verax System MIB.')
products = MibIdentifier((1, 3, 6, 1, 4, 1, 21340, 1))
veraxnms = MibIdentifier((1, 3, 6, 1, 4, 1, 21340, 1, 2))
mibBuilder.exportSymbols("VERAX-MIB", products=products, PYSNMP_MODULE_ID=veraxMIB, veraxMIB=veraxMIB, veraxnms=veraxnms)
