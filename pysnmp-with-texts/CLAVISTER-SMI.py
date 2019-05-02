#
# PySNMP MIB module CLAVISTER-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CLAVISTER-SMI
# Produced by pysmi-0.3.4 at Wed May  1 12:25:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Gauge32, TimeTicks, Counter64, Unsigned32, MibIdentifier, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, NotificationType, enterprises, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "TimeTicks", "Counter64", "Unsigned32", "MibIdentifier", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "NotificationType", "enterprises", "Bits", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
clavisterSmiMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 5089, 0))
clavisterSmiMibModule.setRevisions(('2006-05-19 09:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: clavisterSmiMibModule.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: clavisterSmiMibModule.setLastUpdated('200605190900Z')
if mibBuilder.loadTexts: clavisterSmiMibModule.setOrganization('Clavister AB')
if mibBuilder.loadTexts: clavisterSmiMibModule.setContactInfo('Clavister Support Box 393 SE-891 28 ORNSKOLDSVIK SWEDEN Tel: +46-660-299200 E-mail: support@clavister.com http://www.clavister.com')
if mibBuilder.loadTexts: clavisterSmiMibModule.setDescription('Smi Mib')
clavister = MibIdentifier((1, 3, 6, 1, 4, 1, 5089))
clavisterOS = MibIdentifier((1, 3, 6, 1, 4, 1, 5089, 1))
clavisterOSTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 5089, 1, 0))
clavisterOSTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 5089, 1, 1))
clavisterOSStats = MibIdentifier((1, 3, 6, 1, 4, 1, 5089, 1, 2))
clavisterReg = MibIdentifier((1, 3, 6, 1, 4, 1, 5089, 2))
clavisterMibModules = MibIdentifier((1, 3, 6, 1, 4, 1, 5089, 2, 1))
clavisterMibConfs = MibIdentifier((1, 3, 6, 1, 4, 1, 5089, 2, 2))
clavisterMibObjectGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5089, 2, 3))
mibBuilder.exportSymbols("CLAVISTER-SMI", clavisterReg=clavisterReg, clavisterOS=clavisterOS, clavisterMibObjectGroups=clavisterMibObjectGroups, clavisterMibConfs=clavisterMibConfs, clavister=clavister, clavisterOSTrapInfo=clavisterOSTrapInfo, clavisterSmiMibModule=clavisterSmiMibModule, clavisterOSStats=clavisterOSStats, clavisterMibModules=clavisterMibModules, clavisterOSTrap=clavisterOSTrap, PYSNMP_MODULE_ID=clavisterSmiMibModule)
