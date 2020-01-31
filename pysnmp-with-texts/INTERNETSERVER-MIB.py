#
# PySNMP MIB module INTERNETSERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/tin/Dev/mibs.snmplabs.com/asn1/INTERNETSERVER-MIB
# Produced by pysmi-0.3.4 at Fri Jan 31 21:33:41 2020
# On host bier platform Linux version 5.4.0-3-amd64 by user tin
# Using Python version 3.7.6 (default, Jan 19 2020, 22:34:52) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
software, microsoft = mibBuilder.importSymbols("MSFT-MIB", "software", "microsoft")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, ObjectIdentity, MibIdentifier, ModuleIdentity, iso, NotificationType, Counter64, Gauge32, Unsigned32, enterprises, Integer32, TimeTicks, IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "iso", "NotificationType", "Counter64", "Gauge32", "Unsigned32", "enterprises", "Integer32", "TimeTicks", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
internetServer = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 7))
inetSrvCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 7, 1))
inetSrvStats = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 7, 1, 1))
mibBuilder.exportSymbols("INTERNETSERVER-MIB", inetSrvCommon=inetSrvCommon, inetSrvStats=inetSrvStats, internetServer=internetServer)
