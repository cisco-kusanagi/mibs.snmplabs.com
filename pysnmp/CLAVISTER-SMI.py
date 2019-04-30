#
# PySNMP MIB module CLAVISTER-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CLAVISTER-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 18:09:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Gauge32, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, enterprises, iso, Bits, NotificationType, TimeTicks, IpAddress, Unsigned32, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "enterprises", "iso", "Bits", "NotificationType", "TimeTicks", "IpAddress", "Unsigned32", "Integer32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
clavisterSmiMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 5089, 0))
clavisterSmiMibModule.setRevisions(('2006-05-19 09:00',))
if mibBuilder.loadTexts: clavisterSmiMibModule.setLastUpdated('200605190900Z')
if mibBuilder.loadTexts: clavisterSmiMibModule.setOrganization('Clavister AB')
clavister = MibIdentifier((1, 3, 6, 1, 4, 1, 5089))
clavisterOS = MibIdentifier((1, 3, 6, 1, 4, 1, 5089, 1))
clavisterOSTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 5089, 1, 0))
clavisterOSTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 5089, 1, 1))
clavisterOSStats = MibIdentifier((1, 3, 6, 1, 4, 1, 5089, 1, 2))
clavisterReg = MibIdentifier((1, 3, 6, 1, 4, 1, 5089, 2))
clavisterMibModules = MibIdentifier((1, 3, 6, 1, 4, 1, 5089, 2, 1))
clavisterMibConfs = MibIdentifier((1, 3, 6, 1, 4, 1, 5089, 2, 2))
clavisterMibObjectGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5089, 2, 3))
mibBuilder.exportSymbols("CLAVISTER-SMI", clavisterOSStats=clavisterOSStats, clavisterOSTrap=clavisterOSTrap, clavister=clavister, clavisterMibModules=clavisterMibModules, clavisterMibObjectGroups=clavisterMibObjectGroups, clavisterReg=clavisterReg, clavisterOS=clavisterOS, clavisterOSTrapInfo=clavisterOSTrapInfo, PYSNMP_MODULE_ID=clavisterSmiMibModule, clavisterMibConfs=clavisterMibConfs, clavisterSmiMibModule=clavisterSmiMibModule)
