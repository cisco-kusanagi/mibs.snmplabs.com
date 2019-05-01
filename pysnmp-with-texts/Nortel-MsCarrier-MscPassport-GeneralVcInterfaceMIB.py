#
# PySNMP MIB module Nortel-MsCarrier-MscPassport-GeneralVcInterfaceMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-MsCarrier-MscPassport-GeneralVcInterfaceMIB
# Produced by pysmi-0.3.4 at Wed May  1 14:30:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
mscPassportMIBs, = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB", "mscPassportMIBs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, NotificationType, ObjectIdentity, IpAddress, Bits, TimeTicks, iso, Counter64, Integer32, Gauge32, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "ObjectIdentity", "IpAddress", "Bits", "TimeTicks", "iso", "Counter64", "Integer32", "Gauge32", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
generalVcInterfaceMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 58))
mibBuilder.exportSymbols("Nortel-MsCarrier-MscPassport-GeneralVcInterfaceMIB", generalVcInterfaceMIB=generalVcInterfaceMIB)
