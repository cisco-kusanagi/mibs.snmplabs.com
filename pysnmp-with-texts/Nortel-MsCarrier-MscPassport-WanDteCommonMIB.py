#
# PySNMP MIB module Nortel-MsCarrier-MscPassport-WanDteCommonMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-MsCarrier-MscPassport-WanDteCommonMIB
# Produced by pysmi-0.3.4 at Wed May  1 14:31:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
mscPassportMIBs, = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB", "mscPassportMIBs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Gauge32, ModuleIdentity, Counter32, iso, TimeTicks, Counter64, Unsigned32, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "ModuleIdentity", "Counter32", "iso", "TimeTicks", "Counter64", "Unsigned32", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wanDteCommonMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 52))
mibBuilder.exportSymbols("Nortel-MsCarrier-MscPassport-WanDteCommonMIB", wanDteCommonMIB=wanDteCommonMIB)
