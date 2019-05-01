#
# PySNMP MIB module VOLUBILL-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VOLUBILL-ROOT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:04:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Gauge32, ObjectIdentity, Bits, MibIdentifier, Unsigned32, TimeTicks, NotificationType, IpAddress, Integer32, Counter64, iso, Counter32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "ObjectIdentity", "Bits", "MibIdentifier", "Unsigned32", "TimeTicks", "NotificationType", "IpAddress", "Integer32", "Counter64", "iso", "Counter32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
volubill = MibIdentifier((1, 3, 6, 1, 4, 1, 9905))
vlbProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 9905, 1))
vlbComponents = MibIdentifier((1, 3, 6, 1, 4, 1, 9905, 2))
mibBuilder.exportSymbols("VOLUBILL-ROOT-MIB", vlbComponents=vlbComponents, volubill=volubill, vlbProducts=vlbProducts)
