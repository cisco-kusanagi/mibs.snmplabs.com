#
# PySNMP MIB module Nortel-MsCarrier-MscPassport-GeneralVcInterfaceMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-MsCarrier-MscPassport-GeneralVcInterfaceMIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:20:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
mscPassportMIBs, = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB", "mscPassportMIBs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Bits, NotificationType, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, MibIdentifier, ModuleIdentity, Unsigned32, TimeTicks, ObjectIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "NotificationType", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "MibIdentifier", "ModuleIdentity", "Unsigned32", "TimeTicks", "ObjectIdentity", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
generalVcInterfaceMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 58))
mibBuilder.exportSymbols("Nortel-MsCarrier-MscPassport-GeneralVcInterfaceMIB", generalVcInterfaceMIB=generalVcInterfaceMIB)
