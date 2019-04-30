#
# PySNMP MIB module EdgeSwitch-QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EdgeSwitch-QOS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:56:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
fastPath, = mibBuilder.importSymbols("EdgeSwitch-REF-MIB", "fastPath")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, TimeTicks, IpAddress, Gauge32, ObjectIdentity, Counter32, Integer32, ModuleIdentity, iso, Counter64, Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "TimeTicks", "IpAddress", "Gauge32", "ObjectIdentity", "Counter32", "Integer32", "ModuleIdentity", "iso", "Counter64", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
fastPathQOS = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3))
fastPathQOS.setRevisions(('2011-01-26 00:00', '2007-05-23 00:00', '2003-11-21 00:00', '2002-01-30 15:44',))
if mibBuilder.loadTexts: fastPathQOS.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: fastPathQOS.setOrganization('Broadcom Inc')
mibBuilder.exportSymbols("EdgeSwitch-QOS-MIB", PYSNMP_MODULE_ID=fastPathQOS, fastPathQOS=fastPathQOS)
