#
# PySNMP MIB module CDX6500T1E1-OPT-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CDX6500T1E1-OPT-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 17:30:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
cdx6500PSTPortProtocolGroup, cdx6500PCTPortProtocolGroup = mibBuilder.importSymbols("CDX6500-SMI", "cdx6500PSTPortProtocolGroup", "cdx6500PCTPortProtocolGroup")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, Counter64, ObjectIdentity, ModuleIdentity, Unsigned32, MibIdentifier, IpAddress, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "Counter64", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "MibIdentifier", "IpAddress", "Gauge32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cdx6500PCTT1E1PortTable = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24))
cdx6500PSTT1E1PortTable = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25))
mibBuilder.exportSymbols("CDX6500T1E1-OPT-SMI", cdx6500PCTT1E1PortTable=cdx6500PCTT1E1PortTable, cdx6500PSTT1E1PortTable=cdx6500PSTT1E1PortTable)
