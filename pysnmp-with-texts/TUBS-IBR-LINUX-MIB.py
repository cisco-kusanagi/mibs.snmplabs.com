#
# PySNMP MIB module TUBS-IBR-LINUX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TUBS-IBR-LINUX-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:27:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
TimeTicks, Integer32, IpAddress, ModuleIdentity, Counter64, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ObjectIdentity, Counter32, Unsigned32, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "IpAddress", "ModuleIdentity", "Counter64", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ObjectIdentity", "Counter32", "Unsigned32", "Bits", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ibr, = mibBuilder.importSymbols("TUBS-REGISTRATION", "ibr")
linuxMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1575, 1, 5))
linuxMIB.setRevisions(('1998-01-07 06:22', '1997-02-14 10:23', '1994-11-15 20:24',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: linuxMIB.setRevisionsDescriptions(('Load average object-types added, clarification of linuxCPU.', 'Various cleanups to make the module conforming to SNMPv2 SMI.', 'The initial revision of this module.',))
if mibBuilder.loadTexts: linuxMIB.setLastUpdated('9801070622Z')
if mibBuilder.loadTexts: linuxMIB.setOrganization('TU Braunschweig')
if mibBuilder.loadTexts: linuxMIB.setContactInfo('Juergen Schoenwaelder TU Braunschweig Bueltenweg 74/75 38108 Braunschweig Germany Tel: +49 531 391 3283 Fax: +49 531 391 5936 E-mail: schoenw@ibr.cs.tu-bs.de')
if mibBuilder.loadTexts: linuxMIB.setDescription('Experimental MIB modules for the linux operating system.')
linuxObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 5, 2))
linuxConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 5, 3))
class LoadValue(TextualConvention, Integer32):
    description = 'This data type represents a systems load average over a given time interval. Every usage of this textual convention is required to specify the time interval. A value represents the average number of processes ready to run times 100.'
    status = 'current'
    displayHint = 'd-2'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

linuxCPU = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 5, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linuxCPU.setStatus('current')
if mibBuilder.loadTexts: linuxCPU.setDescription('The identification of the linux CPUs. This string contains foreach CPU present in the system the CPU type, model and vendor (if known by the operating system).')
linuxBogo = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 5, 2, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linuxBogo.setStatus('current')
if mibBuilder.loadTexts: linuxBogo.setDescription('The number of BOGO MIPS of the linux system.')
linuxLoadAvg1 = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 5, 2, 3), LoadValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linuxLoadAvg1.setStatus('current')
if mibBuilder.loadTexts: linuxLoadAvg1.setDescription('The average system load during the last 60 seconds.')
linuxLoadAvg5 = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 5, 2, 4), LoadValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linuxLoadAvg5.setStatus('current')
if mibBuilder.loadTexts: linuxLoadAvg5.setDescription('The average system load during the last 5 minutes.')
linuxLoadAvg15 = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 5, 2, 5), LoadValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linuxLoadAvg15.setStatus('current')
if mibBuilder.loadTexts: linuxLoadAvg15.setDescription('The average system load during the last 15 minutes.')
linuxCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 5, 3, 1))
linuxGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 5, 3, 2))
linuxCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1575, 1, 5, 3, 1, 1)).setObjects(("TUBS-IBR-LINUX-MIB", "linuxGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    linuxCompliance = linuxCompliance.setStatus('current')
if mibBuilder.loadTexts: linuxCompliance.setDescription('The compliance statement for an SNMP entity which implements the linux MIB.')
linuxGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1575, 1, 5, 3, 2, 1)).setObjects(("TUBS-IBR-LINUX-MIB", "linuxCPU"), ("TUBS-IBR-LINUX-MIB", "linuxBogo"), ("TUBS-IBR-LINUX-MIB", "linuxLoadAvg1"), ("TUBS-IBR-LINUX-MIB", "linuxLoadAvg5"), ("TUBS-IBR-LINUX-MIB", "linuxLoadAvg15"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    linuxGroup = linuxGroup.setStatus('current')
if mibBuilder.loadTexts: linuxGroup.setDescription('A collection of linux specific objects.')
mibBuilder.exportSymbols("TUBS-IBR-LINUX-MIB", PYSNMP_MODULE_ID=linuxMIB, linuxBogo=linuxBogo, linuxObjects=linuxObjects, linuxCPU=linuxCPU, linuxCompliance=linuxCompliance, linuxMIB=linuxMIB, linuxGroups=linuxGroups, LoadValue=LoadValue, linuxLoadAvg15=linuxLoadAvg15, linuxCompliances=linuxCompliances, linuxGroup=linuxGroup, linuxLoadAvg1=linuxLoadAvg1, linuxConformance=linuxConformance, linuxLoadAvg5=linuxLoadAvg5)
