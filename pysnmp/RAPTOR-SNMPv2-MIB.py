#
# PySNMP MIB module RAPTOR-SNMPv2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RAPTOR-SNMPv2-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:43:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, iso, MibIdentifier, NotificationType, ObjectIdentity, Gauge32, Integer32, ModuleIdentity, Bits, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "iso", "MibIdentifier", "NotificationType", "ObjectIdentity", "Gauge32", "Integer32", "ModuleIdentity", "Bits", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
raptorSystems = MibIdentifier((1, 3, 6, 1, 4, 1, 1294))
raptorModules = MibIdentifier((1, 3, 6, 1, 4, 1, 1294, 1))
raptorObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1294, 2))
raptorTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1294, 3))
raptorNotify = ModuleIdentity((1, 3, 6, 1, 4, 1, 1294, 1, 1))
raptorNotify.setRevisions(('1998-10-27 12:00',))
if mibBuilder.loadTexts: raptorNotify.setLastUpdated('9810271200Z')
if mibBuilder.loadTexts: raptorNotify.setOrganization('Axent Technologies, Inc. Raptor SBU')
raptorNotifyMessage = MibScalar((1, 3, 6, 1, 4, 1, 1294, 2, 1), OctetString())
if mibBuilder.loadTexts: raptorNotifyMessage.setStatus('current')
raptorNotifyTrap = NotificationType((1, 3, 6, 1, 4, 1, 1294, 3, 1)).setObjects(("RAPTOR-SNMPv2-MIB", "raptorNotifyMessage"))
if mibBuilder.loadTexts: raptorNotifyTrap.setStatus('current')
mibBuilder.exportSymbols("RAPTOR-SNMPv2-MIB", raptorNotify=raptorNotify, raptorNotifyMessage=raptorNotifyMessage, raptorModules=raptorModules, raptorSystems=raptorSystems, raptorNotifyTrap=raptorNotifyTrap, raptorTraps=raptorTraps, PYSNMP_MODULE_ID=raptorNotify, raptorObjects=raptorObjects)
