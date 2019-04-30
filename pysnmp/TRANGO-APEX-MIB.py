#
# PySNMP MIB module TRANGO-APEX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRANGO-APEX-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:19:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, ObjectIdentity, ModuleIdentity, Counter32, IpAddress, MibIdentifier, enterprises, Bits, NotificationType, iso, Counter64, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "Counter32", "IpAddress", "MibIdentifier", "enterprises", "Bits", "NotificationType", "iso", "Counter64", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
trango = MibIdentifier((1, 3, 6, 1, 4, 1, 5454))
tbw = MibIdentifier((1, 3, 6, 1, 4, 1, 5454, 1))
apex = MibIdentifier((1, 3, 6, 1, 4, 1, 5454, 1, 60))
mibBuilder.exportSymbols("TRANGO-APEX-MIB", apex=apex, tbw=tbw, trango=trango)
