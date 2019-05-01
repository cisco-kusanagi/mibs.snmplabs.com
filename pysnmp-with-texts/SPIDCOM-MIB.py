#
# PySNMP MIB module SPIDCOM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SPIDCOM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:17:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Bits, ModuleIdentity, NotificationType, Unsigned32, Integer32, IpAddress, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Counter32, ObjectIdentity, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "ModuleIdentity", "NotificationType", "Unsigned32", "Integer32", "IpAddress", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Counter32", "ObjectIdentity", "MibIdentifier", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
spidcom = MibIdentifier((1, 3, 6, 1, 4, 1, 22764))
mibBuilder.exportSymbols("SPIDCOM-MIB", spidcom=spidcom)
