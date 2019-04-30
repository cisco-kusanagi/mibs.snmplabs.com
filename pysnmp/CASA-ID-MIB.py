#
# PySNMP MIB module CASA-ID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CASA-ID-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:29:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
casa, = mibBuilder.importSymbols("CASA-MIB", "casa")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, MibIdentifier, Bits, TimeTicks, IpAddress, NotificationType, iso, ObjectIdentity, Gauge32, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "MibIdentifier", "Bits", "TimeTicks", "IpAddress", "NotificationType", "iso", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
casaIdMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 20858, 2))
casaIdMib.setRevisions(('1900-04-07 00:00',))
if mibBuilder.loadTexts: casaIdMib.setLastUpdated('200608150000Z')
if mibBuilder.loadTexts: casaIdMib.setOrganization('CASA SYSTEMS INC')
casa2100System = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 2, 1))
casa2200System = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 2, 20))
casa2300System = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 2, 30))
casa2800System = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 2, 40))
casa3000System = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 2, 50))
casa6000System = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 2, 100))
casa10000System = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 2, 200))
mibBuilder.exportSymbols("CASA-ID-MIB", casa2200System=casa2200System, casa2800System=casa2800System, casa2100System=casa2100System, casa2300System=casa2300System, casa6000System=casa6000System, casa3000System=casa3000System, PYSNMP_MODULE_ID=casaIdMib, casaIdMib=casaIdMib, casa10000System=casa10000System)
