#
# PySNMP MIB module ADTRAN-AOS-OVER-TEMP-PROTECTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ADTRAN-AOS-OVER-TEMP-PROTECTION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:14:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
adGenAOSCommon, adGenAOSConformance = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSCommon", "adGenAOSConformance")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, MibIdentifier, NotificationType, ObjectIdentity, ModuleIdentity, Unsigned32, iso, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "NotificationType", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "iso", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "Gauge32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adGenAOSOverTempProtectionMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 1, 10))
adGenAOSOverTempProtectionMib.setRevisions(('2014-11-04 16:15',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: adGenAOSOverTempProtectionMib.setRevisionsDescriptions(('Created the adGenAosOverTempProtection MIB. Revision R11.6',))
if mibBuilder.loadTexts: adGenAOSOverTempProtectionMib.setLastUpdated('201411041615Z')
if mibBuilder.loadTexts: adGenAOSOverTempProtectionMib.setOrganization('ADTRAN, Inc.')
if mibBuilder.loadTexts: adGenAOSOverTempProtectionMib.setContactInfo(' Technical Support Dept. Postal: ADTRAN, Inc. 901 Explorer Blvd. Huntsville, AL 35806 Tel: +1 800 726-8663 Fax: +1 256 963 6217 E-mail: support@adtran.com')
if mibBuilder.loadTexts: adGenAOSOverTempProtectionMib.setDescription('The MIB module defines over-temperature configuration information and traps for AdtranOS products.')
adGenAOSOverTempProtection = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 10))
adGenAOSOverTempProtectionTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 10, 0))
adGenAOSOverTempProtectionWarning = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 10, 0, 1))
if mibBuilder.loadTexts: adGenAOSOverTempProtectionWarning.setStatus('current')
if mibBuilder.loadTexts: adGenAOSOverTempProtectionWarning.setDescription('An over-temperature warning trap signifies that the warning temperature threshold has been exceeded.')
adGenAOSOverTempProtectionShutdown = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 10, 0, 2))
if mibBuilder.loadTexts: adGenAOSOverTempProtectionShutdown.setStatus('current')
if mibBuilder.loadTexts: adGenAOSOverTempProtectionShutdown.setDescription('An over-temperature shutdown trap signifies that the shutdown temperature threshold has been exceeded, and the unit will restart into low-power mode.')
adGenAOSOverTempProtectionConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 19))
adGenAOSOverTempProtectionGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 19, 1))
adGenAOSOverTempProtectionCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 19, 2))
adGenAOSOverTempProtectionFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 19, 2, 1)).setObjects(("ADTRAN-AOS-OVER-TEMP-PROTECTION-MIB", "adGenAOSOverTempProtectionNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSOverTempProtectionFullCompliance = adGenAOSOverTempProtectionFullCompliance.setStatus('current')
if mibBuilder.loadTexts: adGenAOSOverTempProtectionFullCompliance.setDescription('The compliance statement for SNMP entities which implement version 2 of the adGenAosOverTempProtection MIB. When the implementation of this MIB supports adGenAOSOverTempProtectionNotificationGroup, then such an implementation can claim full compliance.')
adGenAOSOverTempProtectionNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 19, 1, 1)).setObjects(("ADTRAN-AOS-OVER-TEMP-PROTECTION-MIB", "adGenAOSOverTempProtectionWarning"), ("ADTRAN-AOS-OVER-TEMP-PROTECTION-MIB", "adGenAOSOverTempProtectionShutdown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSOverTempProtectionNotificationGroup = adGenAOSOverTempProtectionNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: adGenAOSOverTempProtectionNotificationGroup.setDescription("Traps which may be used to enhance event driven management of the chassis's over-temperature protection subsystem.")
mibBuilder.exportSymbols("ADTRAN-AOS-OVER-TEMP-PROTECTION-MIB", adGenAOSOverTempProtectionGroups=adGenAOSOverTempProtectionGroups, adGenAOSOverTempProtectionNotificationGroup=adGenAOSOverTempProtectionNotificationGroup, adGenAOSOverTempProtection=adGenAOSOverTempProtection, adGenAOSOverTempProtectionConformance=adGenAOSOverTempProtectionConformance, adGenAOSOverTempProtectionTrap=adGenAOSOverTempProtectionTrap, adGenAOSOverTempProtectionShutdown=adGenAOSOverTempProtectionShutdown, adGenAOSOverTempProtectionMib=adGenAOSOverTempProtectionMib, adGenAOSOverTempProtectionCompliances=adGenAOSOverTempProtectionCompliances, adGenAOSOverTempProtectionFullCompliance=adGenAOSOverTempProtectionFullCompliance, adGenAOSOverTempProtectionWarning=adGenAOSOverTempProtectionWarning, PYSNMP_MODULE_ID=adGenAOSOverTempProtectionMib)
