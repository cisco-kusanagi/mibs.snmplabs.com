#
# PySNMP MIB module MSFT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MSFT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:58:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Integer32, enterprises, Unsigned32, Bits, Counter32, NotificationType, TimeTicks, Gauge32, ModuleIdentity, MibIdentifier, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "enterprises", "Unsigned32", "Bits", "Counter32", "NotificationType", "TimeTicks", "Gauge32", "ModuleIdentity", "MibIdentifier", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
microsoft = MibIdentifier((1, 3, 6, 1, 4, 1, 311))
software = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1))
systems = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 1))
os = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 1, 3))
windowsNT = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1))
windows = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 2))
workstation = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1))
server = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 2))
dc = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 3))
mibBuilder.exportSymbols("MSFT-MIB", server=server, software=software, os=os, microsoft=microsoft, workstation=workstation, windows=windows, systems=systems, windowsNT=windowsNT, dc=dc)
