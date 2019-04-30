#
# PySNMP MIB module RADLAN-ENDOFMIB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-ENDOFMIB-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:38:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Counter64, ObjectIdentity, Gauge32, Unsigned32, ModuleIdentity, Integer32, Counter32, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "ModuleIdentity", "Integer32", "Counter32", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rndEndOfMibGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 1000))
rndEndOfMibGroup.setRevisions(('2007-01-02 00:00',))
if mibBuilder.loadTexts: rndEndOfMibGroup.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rndEndOfMibGroup.setOrganization('Radlan - a MARVELL company. Marvell Semiconductor, Inc.')
rndEndOfMib = MibScalar((1, 3, 6, 1, 4, 1, 89, 1000, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rndEndOfMib.setStatus('current')
mibBuilder.exportSymbols("RADLAN-ENDOFMIB-MIB", rndEndOfMibGroup=rndEndOfMibGroup, rndEndOfMib=rndEndOfMib, PYSNMP_MODULE_ID=rndEndOfMibGroup)
