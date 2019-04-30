#
# PySNMP MIB module Nortel-MsCarrier-MscPassport-TimMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-MsCarrier-MscPassport-TimMIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:22:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
mscPassportMIBs, = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB", "mscPassportMIBs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Unsigned32, ModuleIdentity, MibIdentifier, Integer32, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, Counter64, IpAddress, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "ModuleIdentity", "MibIdentifier", "Integer32", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "Counter64", "IpAddress", "Gauge32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
timMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 102))
mibBuilder.exportSymbols("Nortel-MsCarrier-MscPassport-TimMIB", timMIB=timMIB)
