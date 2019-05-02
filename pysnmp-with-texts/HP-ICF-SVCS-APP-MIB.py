#
# PySNMP MIB module HP-ICF-SVCS-APP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-SVCS-APP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:35:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Gauge32, Integer32, TimeTicks, iso, NotificationType, MibIdentifier, Bits, IpAddress, Counter64, ObjectIdentity, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "TimeTicks", "iso", "NotificationType", "MibIdentifier", "Bits", "IpAddress", "Counter64", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
AutonomousType, MacAddress, DisplayString, TruthValue, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "AutonomousType", "MacAddress", "DisplayString", "TruthValue", "TextualConvention", "RowStatus")
hpicfSvcsAppMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86))
hpicfSvcsAppMIB.setRevisions(('2011-05-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpicfSvcsAppMIB.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: hpicfSvcsAppMIB.setLastUpdated('201105270000Z')
if mibBuilder.loadTexts: hpicfSvcsAppMIB.setOrganization('HP Networking')
if mibBuilder.loadTexts: hpicfSvcsAppMIB.setContactInfo('Hewlett Packard Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfSvcsAppMIB.setDescription('This MIB manages various parameters of services module applications.')
hpicfSvcsAppNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 0))
hpicfSvcsAppObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1))
hpicfSvcsAppConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 2))
class AppStatus(TextualConvention, Integer32):
    description = 'Status of the Services module application. The value other(1) represents the application status is other than one of the states below. The value unknown(2) represents the application status is in Unknown state such as uninitialized. The value bootinit(3) represents the boot process is initializing. The value booting(4) represents the application is in Process of booting. The value boot failure(5) represents the application has failed to Boot for some reason. The value halted(6) represents the application has been shutdown and/or halted. The value rebooting(7) represents the application is rebooting. The value ready(8) represents the platform OS is ready to run an application. The value appInit(9) represents the application is initializing. The value appError(10) represents the application has errored/failed. The value appRunning(11) represents the application is running. The value shuttingDown(12) represents the application is shutting down.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("bootInit", 3), ("booting", 4), ("bootFailure", 5), ("halted", 6), ("rebooting", 7), ("ready", 8), ("appInit", 9), ("appError", 10), ("appRunning", 11), ("shuttingDown", 12))

hpicfSvcsInstalledAppTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 1), )
if mibBuilder.loadTexts: hpicfSvcsInstalledAppTable.setStatus('current')
if mibBuilder.loadTexts: hpicfSvcsInstalledAppTable.setDescription('Table of installed services application images.')
hpicfSvcsInstalledAppEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hpicfSvcsInstalledAppEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfSvcsInstalledAppEntry.setDescription('An entry in the services installed application table.')
hpicfSvcsInstalledAppPlatformType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 1, 1, 1), AutonomousType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSvcsInstalledAppPlatformType.setStatus('current')
if mibBuilder.loadTexts: hpicfSvcsInstalledAppPlatformType.setDescription('An object that points to the Services platform type. If the value is unknown by this agent, then the value { 0 0 } is returned.')
hpicfSvcsInstalledAppDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSvcsInstalledAppDescription.setStatus('current')
if mibBuilder.loadTexts: hpicfSvcsInstalledAppDescription.setDescription('Description of the application. Can include specific information regarding this application including model or product name.')
hpicfSvcsInstalledAppVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSvcsInstalledAppVersion.setStatus('current')
if mibBuilder.loadTexts: hpicfSvcsInstalledAppVersion.setDescription('Version of the installed application.')
hpicfSvcsInstalledAppStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 1, 1, 4), AppStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSvcsInstalledAppStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfSvcsInstalledAppStatus.setDescription('Status of the installed services application.')
hpicfSvcsInstalledAppJNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 1, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSvcsInstalledAppJNumber.setStatus('current')
if mibBuilder.loadTexts: hpicfSvcsInstalledAppJNumber.setDescription('J-Number of the installed services application.')
hpicfSvcsInstalledAppLicensingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("expired", 2), ("unknown", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSvcsInstalledAppLicensingStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfSvcsInstalledAppLicensingStatus.setDescription('Licensing status of the installed services application. A value active(1), represents the licensing status is available and active. A value expired(2), represents the licensing status is available and expired. A value unknown(3), represents the licensing status is not available.')
hpicfSvcsInstalledAppRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSvcsInstalledAppRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfSvcsInstalledAppRowStatus.setDescription('This object permits management of the table by facilitating actions such as row creation, construction, and destruction. The value of this object has no effect on whether other objects in this conceptual row can be modified.')
hpicfSvcsV1AppTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 2), )
if mibBuilder.loadTexts: hpicfSvcsV1AppTable.setStatus('current')
if mibBuilder.loadTexts: hpicfSvcsV1AppTable.setDescription('Version 1 table of Active application connections to Switch services.')
hpicfSvcsV1AppEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hpicfSvcsV1AppEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfSvcsV1AppEntry.setDescription('An entry in the version 1 application table.')
hpicfSvcsV1AppIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSvcsV1AppIndex.setStatus('current')
if mibBuilder.loadTexts: hpicfSvcsV1AppIndex.setDescription('Index of the Version 1 services application.')
hpicfSvcsV1AppCLIAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 2, 1, 2), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSvcsV1AppCLIAvailable.setStatus('current')
if mibBuilder.loadTexts: hpicfSvcsV1AppCLIAvailable.setDescription('CLI status of the Version 1 services application.')
hpicfSvcsV1AppName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 2, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSvcsV1AppName.setStatus('current')
if mibBuilder.loadTexts: hpicfSvcsV1AppName.setDescription('Name of the application. Each application is uniquely identified by its name. If application name is not available, a string of size zero will be returned.')
hpicfSvcsV1AppDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 2, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSvcsV1AppDescription.setStatus('current')
if mibBuilder.loadTexts: hpicfSvcsV1AppDescription.setDescription('Description of the application. Can include specific information regarding this application including model or product name.')
hpicfSvcsV1AppVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 2, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSvcsV1AppVersion.setStatus('current')
if mibBuilder.loadTexts: hpicfSvcsV1AppVersion.setDescription('Version of the Version 1 application. A string of size zero will be returned if the Version 1 application version is not available,.')
hpicfSvcsV1AppStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 2, 1, 6), AppStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSvcsV1AppStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfSvcsV1AppStatus.setDescription('Status of the Version 1 services application.')
hpicfSvcsV1AppJNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 2, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSvcsV1AppJNumber.setStatus('current')
if mibBuilder.loadTexts: hpicfSvcsV1AppJNumber.setDescription('J-Number of the Version 1 services application.')
hpicfSvcsV1AppURL = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 2, 1, 8), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSvcsV1AppURL.setStatus('current')
if mibBuilder.loadTexts: hpicfSvcsV1AppURL.setDescription('URL of the Version 1 services application. A string of size zero will be returned if the Version 1 application URL is not available.')
hpicfSvcsV1AppRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 2, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSvcsV1AppRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfSvcsV1AppRowStatus.setDescription('This object permits management of the table by facilitating actions such as row creation, construction, and destruction. The value of this object has no effect on whether other objects in this conceptual row can be modified.')
hpicfSvcsAppCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 2, 1))
hpicfSvcsAppGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 2, 2))
hpicfSvcsAppCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 2, 1, 1)).setObjects(("HP-ICF-SVCS-APP-MIB", "hpicfSvcsInstalledAppGroup"), ("HP-ICF-SVCS-APP-MIB", "hpicfSvcsV1AppGroup"), ("HP-ICF-SVCS-APP-MIB", "hpicfSvcsInstalledAppGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSvcsAppCompliance = hpicfSvcsAppCompliance.setStatus('current')
if mibBuilder.loadTexts: hpicfSvcsAppCompliance.setDescription('The compliance statement for HP routers implementing the HP-ICF-SVCS-APP-MIB.')
hpicfSvcsInstalledAppGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 2, 2, 1)).setObjects(("HP-ICF-SVCS-APP-MIB", "hpicfSvcsInstalledAppPlatformType"), ("HP-ICF-SVCS-APP-MIB", "hpicfSvcsInstalledAppDescription"), ("HP-ICF-SVCS-APP-MIB", "hpicfSvcsInstalledAppVersion"), ("HP-ICF-SVCS-APP-MIB", "hpicfSvcsInstalledAppStatus"), ("HP-ICF-SVCS-APP-MIB", "hpicfSvcsInstalledAppJNumber"), ("HP-ICF-SVCS-APP-MIB", "hpicfSvcsInstalledAppLicensingStatus"), ("HP-ICF-SVCS-APP-MIB", "hpicfSvcsInstalledAppRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSvcsInstalledAppGroup = hpicfSvcsInstalledAppGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfSvcsInstalledAppGroup.setDescription('Services installed application group objects.')
hpicfSvcsV1AppGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 2, 2, 2)).setObjects(("HP-ICF-SVCS-APP-MIB", "hpicfSvcsV1AppIndex"), ("HP-ICF-SVCS-APP-MIB", "hpicfSvcsV1AppCLIAvailable"), ("HP-ICF-SVCS-APP-MIB", "hpicfSvcsV1AppName"), ("HP-ICF-SVCS-APP-MIB", "hpicfSvcsV1AppDescription"), ("HP-ICF-SVCS-APP-MIB", "hpicfSvcsV1AppVersion"), ("HP-ICF-SVCS-APP-MIB", "hpicfSvcsV1AppStatus"), ("HP-ICF-SVCS-APP-MIB", "hpicfSvcsV1AppJNumber"), ("HP-ICF-SVCS-APP-MIB", "hpicfSvcsV1AppURL"), ("HP-ICF-SVCS-APP-MIB", "hpicfSvcsV1AppRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSvcsV1AppGroup = hpicfSvcsV1AppGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfSvcsV1AppGroup.setDescription('Services Version 1 application group objects.')
mibBuilder.exportSymbols("HP-ICF-SVCS-APP-MIB", hpicfSvcsV1AppJNumber=hpicfSvcsV1AppJNumber, hpicfSvcsV1AppURL=hpicfSvcsV1AppURL, hpicfSvcsV1AppEntry=hpicfSvcsV1AppEntry, PYSNMP_MODULE_ID=hpicfSvcsAppMIB, AppStatus=AppStatus, hpicfSvcsAppNotifications=hpicfSvcsAppNotifications, hpicfSvcsInstalledAppJNumber=hpicfSvcsInstalledAppJNumber, hpicfSvcsV1AppGroup=hpicfSvcsV1AppGroup, hpicfSvcsAppConformance=hpicfSvcsAppConformance, hpicfSvcsV1AppStatus=hpicfSvcsV1AppStatus, hpicfSvcsInstalledAppDescription=hpicfSvcsInstalledAppDescription, hpicfSvcsAppGroups=hpicfSvcsAppGroups, hpicfSvcsInstalledAppGroup=hpicfSvcsInstalledAppGroup, hpicfSvcsAppCompliances=hpicfSvcsAppCompliances, hpicfSvcsInstalledAppEntry=hpicfSvcsInstalledAppEntry, hpicfSvcsAppCompliance=hpicfSvcsAppCompliance, hpicfSvcsInstalledAppLicensingStatus=hpicfSvcsInstalledAppLicensingStatus, hpicfSvcsAppObjects=hpicfSvcsAppObjects, hpicfSvcsInstalledAppTable=hpicfSvcsInstalledAppTable, hpicfSvcsV1AppTable=hpicfSvcsV1AppTable, hpicfSvcsAppMIB=hpicfSvcsAppMIB, hpicfSvcsInstalledAppPlatformType=hpicfSvcsInstalledAppPlatformType, hpicfSvcsV1AppVersion=hpicfSvcsV1AppVersion, hpicfSvcsInstalledAppVersion=hpicfSvcsInstalledAppVersion, hpicfSvcsV1AppDescription=hpicfSvcsV1AppDescription, hpicfSvcsInstalledAppStatus=hpicfSvcsInstalledAppStatus, hpicfSvcsV1AppCLIAvailable=hpicfSvcsV1AppCLIAvailable, hpicfSvcsV1AppRowStatus=hpicfSvcsV1AppRowStatus, hpicfSvcsV1AppIndex=hpicfSvcsV1AppIndex, hpicfSvcsInstalledAppRowStatus=hpicfSvcsInstalledAppRowStatus, hpicfSvcsV1AppName=hpicfSvcsV1AppName)
