#
# PySNMP MIB module CDX6500T1E1-OPT-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CDX6500T1E1-OPT-SMI
# Produced by pysmi-0.3.4 at Wed May  1 11:47:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
cdx6500PCTPortProtocolGroup, cdx6500PSTPortProtocolGroup = mibBuilder.importSymbols("CDX6500-SMI", "cdx6500PCTPortProtocolGroup", "cdx6500PSTPortProtocolGroup")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Integer32, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, iso, ObjectIdentity, ModuleIdentity, Unsigned32, IpAddress, MibIdentifier, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "iso", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "IpAddress", "MibIdentifier", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cdx6500PCTT1E1PortTable = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24))
cdx6500PSTT1E1PortTable = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25))
mibBuilder.exportSymbols("CDX6500T1E1-OPT-SMI", cdx6500PSTT1E1PortTable=cdx6500PSTT1E1PortTable, cdx6500PCTT1E1PortTable=cdx6500PCTT1E1PortTable)
