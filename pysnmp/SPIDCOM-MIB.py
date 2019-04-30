#
# PySNMP MIB module SPIDCOM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SPIDCOM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:08:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, NotificationType, ModuleIdentity, IpAddress, Counter64, Bits, iso, Integer32, Counter32, ObjectIdentity, MibIdentifier, enterprises, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "NotificationType", "ModuleIdentity", "IpAddress", "Counter64", "Bits", "iso", "Integer32", "Counter32", "ObjectIdentity", "MibIdentifier", "enterprises", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
spidcom = MibIdentifier((1, 3, 6, 1, 4, 1, 22764))
mibBuilder.exportSymbols("SPIDCOM-MIB", spidcom=spidcom)
