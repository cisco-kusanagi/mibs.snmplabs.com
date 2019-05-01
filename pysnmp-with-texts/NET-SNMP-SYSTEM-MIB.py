#
# PySNMP MIB module NET-SNMP-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NET-SNMP-SYSTEM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:18:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
netSnmpObjects, netSnmpModuleIDs = mibBuilder.importSymbols("NET-SNMP-MIB", "netSnmpObjects", "netSnmpModuleIDs")
Float, = mibBuilder.importSymbols("NET-SNMP-TC", "Float")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, ObjectIdentity, Gauge32, NotificationType, Bits, Counter32, ModuleIdentity, Integer32, Unsigned32, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ObjectIdentity", "Gauge32", "NotificationType", "Bits", "Counter32", "ModuleIdentity", "Integer32", "Unsigned32", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
netSnmpSystemMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8072, 3, 1, 4))
netSnmpSystemMIB.setRevisions(('2002-02-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: netSnmpSystemMIB.setRevisionsDescriptions(('First draft.',))
if mibBuilder.loadTexts: netSnmpSystemMIB.setLastUpdated('200202090000Z')
if mibBuilder.loadTexts: netSnmpSystemMIB.setOrganization('www.net-snmp.org')
if mibBuilder.loadTexts: netSnmpSystemMIB.setContactInfo('postal: Wes Hardaker P.O. Box 382 Davis CA 95617 email: net-snmp-coders@lists.sourceforge.net')
if mibBuilder.loadTexts: netSnmpSystemMIB.setDescription('Characteristics of the current running system')
nsMemory = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 31))
nsSwap = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 32))
nsCPU = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 33))
nsLoad = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 34))
nsDiskIO = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 35))
mibBuilder.exportSymbols("NET-SNMP-SYSTEM-MIB", PYSNMP_MODULE_ID=netSnmpSystemMIB, nsDiskIO=nsDiskIO, nsCPU=nsCPU, nsMemory=nsMemory, nsLoad=nsLoad, netSnmpSystemMIB=netSnmpSystemMIB, nsSwap=nsSwap)
